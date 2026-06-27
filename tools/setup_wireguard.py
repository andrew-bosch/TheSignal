#!/usr/bin/env python3
import os
import subprocess
import urllib.request
import sys

PORT = 51280
INTERFACE = "wlan0"
SERVER_IP = "10.8.0.1/24"
CLIENT_IP = "10.8.0.2/24"
CLIENT_IP_ROUTE = "10.8.0.2/32"

def run(cmd, check=True):
    print(f"Executing: {' '.join(cmd)}")
    return subprocess.run(cmd, check=check, capture_output=True, text=True)

def setup_wireguard():
    print("=== Installing WireGuard and Qrencode ===")
    run(["sudo", "apt-get", "update"])
    run(["sudo", "apt-get", "install", "-y", "wireguard", "iptables", "qrencode"])

    print("=== Generating Keys ===")
    # Generate Server Keys
    server_priv = run(["wg", "genkey"]).stdout.strip()
    p = subprocess.Popen(["wg", "pubkey"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    server_pub, _ = p.communicate(input=server_priv)
    server_pub = server_pub.strip()

    # Generate Client Keys
    client_priv = run(["wg", "genkey"]).stdout.strip()
    p = subprocess.Popen(["wg", "pubkey"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    client_pub, _ = p.communicate(input=client_priv)
    client_pub = client_pub.strip()

    print("=== Writing Server Configuration ===")
    server_conf = f"""[Interface]
PrivateKey = {server_priv}
Address = {SERVER_IP}
ListenPort = {PORT}

# Set up NAT routing so client can access local network and internet
PostUp = iptables -A FORWARD -i %i -j ACCEPT; iptables -A FORWARD -o %i -j ACCEPT; iptables -t nat -A POSTROUTING -o {INTERFACE} -j MASQUERADE
PostDown = iptables -D FORWARD -i %i -j ACCEPT; iptables -D FORWARD -o %i -j ACCEPT; iptables -t nat -D POSTROUTING -o {INTERFACE} -j MASQUERADE

[Peer]
PublicKey = {client_pub}
AllowedIPs = {CLIENT_IP_ROUTE}
"""
    # Write configuration
    temp_server_path = "/tmp/wg0.conf"
    with open(temp_server_path, "w") as f:
        f.write(server_conf)
    
    run(["sudo", "mv", temp_server_path, "/etc/wireguard/wg0.conf"])
    run(["sudo", "chmod", "600", "/etc/wireguard/wg0.conf"])

    print("=== Enabling Packet Forwarding ===")
    # Enable IPv4 Forwarding dynamically
    run(["sudo", "sysctl", "-w", "net.ipv4.ip_forward=1"])
    
    # Make it persistent in /etc/sysctl.d/
    sysctl_conf = "net.ipv4.ip_forward=1\n"
    temp_sysctl_path = "/tmp/99-wireguard-forward.conf"
    with open(temp_sysctl_path, "w") as f:
        f.write(sysctl_conf)
    run(["sudo", "mv", temp_sysctl_path, "/etc/sysctl.d/99-wireguard-forward.conf"])

    print("=== Enabling and Starting WireGuard Service ===")
    run(["sudo", "systemctl", "enable", "wg-quick@wg0"])
    run(["sudo", "systemctl", "restart", "wg-quick@wg0"])

    print("=== Fetching Public WAN IP ===")
    try:
        req = urllib.request.Request(
            "https://api.ipify.org", 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            public_ip = response.read().decode('utf-8').strip()
    except Exception as e:
        print(f"Warning: Could not fetch public IP automatically ({e}). Using placeholder 'YOUR_PUBLIC_IP'.")
        public_ip = "YOUR_PUBLIC_IP"

    print(f"Detected Public IP: {public_ip}")

    print("=== Generating Client Configuration ===")
    client_conf = f"""[Interface]
PrivateKey = {client_priv}
Address = {CLIENT_IP}
DNS = 1.1.1.1, 8.8.8.8

[Peer]
PublicKey = {server_pub}
Endpoint = {public_ip}:{PORT}
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
"""
    client_conf_path = os.path.expanduser("~/client.conf")
    with open(client_conf_path, "w") as f:
        f.write(client_conf)
    os.chmod(client_conf_path, 0o600)
    print(f"Client configuration saved to {client_conf_path}")
    print("\n" + "="*60)
    print("WIREGUARD SETUP SUCCESSFUL!")
    print("="*60 + "\n")

if __name__ == "__main__":
    setup_wireguard()
