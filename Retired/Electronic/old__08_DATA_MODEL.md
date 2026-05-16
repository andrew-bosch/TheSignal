# THE SIGNAL — Game State Data Model

**Document:** 08  
**Status:** Complete — TypeScript Schema v0.2

---

## Design Principles

1. **ARBITER is the only writer of authoritative state** — terminals read, propose actions, ARBITER writes
2. **Every state change is an event** — state is never mutated directly; events are appended to an event log; current state is derived from the event log
3. **Public and private state are explicitly separated** — every field is tagged with its visibility scope
4. **The event log is the truth** — any moment in any session can be reconstructed from the event log

---

## Schema Overview

```typescript
// ============================================
// ARBITER GAME STATE — COMPLETE DATA MODEL
// Version 0.2 — Full Integration
// ============================================

// ============================================
// PRIMITIVE TYPES AND IDENTIFIERS
// ============================================

type CovenantID = string;
type SessionID = string;
type RoundID = string;
type FactionID =
  | "architect"
  | "ghost"
  | "syndicate"
  | "signal"
  | "warden";
type OperatorID = string;
type PlayerID = string;
type HexID = string;
type CardID = string;
type AssetID = string;
type ActionID = string;
type AccordID = string;
type AudioCueID = string;
type BleedEffectID = string;

// ============================================
// ENUMERATIONS
// ============================================

type Layer = 1 | 2 | 3 | 4;

type EffectivenessLevel =
  | "peripheral"    // 0-1
  | "functional"    // 2-3
  | "established"   // 4-5
  | "dominant";     // 6+

type ResourceType =
  | "capital"
  | "infrastructure"
  | "signal"
  | "intelligence"
  | "influence_operational"
  | "influence_public";

type PopularityState =
  | "celebrated"
  | "respected"
  | "neutral"
  | "suspect"
  | "discredited";

type CardType =
  | "contact"
  | "equipment"
  | "operation"
  | "intelligence"
  | "event"
  | "legacy"
  | "counter";

type ActionType =
  // Physical Layer 1
  | "physical_intrusion"
  | "physical_theft"
  | "build_structure"
  | "contest_district"
  // Social Layer 2
  | "recruit_asset"
  | "confidence_scheme"
  | "social_engineering"
  | "propaganda_positive"
  | "propaganda_opposition"
  | "propaganda_disinformation"
  | "propaganda_leak"
  | "propaganda_ideological"
  | "crisis_management"
  // Informational Layer 3
  | "data_theft"
  | "intercept"
  | "surveillance_install"
  | "plant_false_data"
  | "counter_surveillance"
  // Digital Layer 4
  | "hack"
  | "deploy_autonomous"
  | "deep_intercept"
  | "purge"
  // Communication
  | "send_message"
  | "propose_accord"
  | "confirm_accord"
  | "breach_accord"
  // Board
  | "place_token"
  // Meta
  | "activate_card"
  | "direct_asset"
  | "use_operator_ability"
  | "public_build"
  | "public_contest"
  | "public_investigate"
  | "public_broadcast"
  | "public_pass"
  | "propose_table_question"
  | "vote_table_question"
  | "resource_trade"
  | "arbiter_conversion"
  | "asset_liquidation"
  | "declare_done";

type PhaseType =
  | "upkeep"
  | "placement"
  | "private_actions"
  | "public_actions"
  | "resolution"
  | "debrief"
  | "scoring"
  | "pre_session"
  | "post_session";

type PlayMode =
  | "competitive"
  | "team"
  | "cooperative"
  | "faction_share"
  | "solo";

type AmbientPowerTier =
  | "passive"
  | "active"
  | "director";

type LoyaltyLevel =
  | "devoted"     // 5
  | "loyal"       // 4
  | "reliable"    // 3
  | "wavering"    // 2
  | "critical"    // 1
  | "burned";     // 0

type ExposureLevel = 0 | 1 | 2 | 3;

type UnlockTier =
  | "awakening"
  | "ascendant"
  | "apex";

type DoctrineAlignment =
  | "strong"
  | "neutral"
  | "weak"
  | "contradiction";

type PortraitQuality =
  | "fractured"       // 0-2
  | "conflicted"      // 3-4
  | "complex"         // 5-6
  | "coherent"        // 7-8
  | "transcendent";   // 9-10

type VisibilityScope =
  | "public"
  | "faction"
  | "player"
  | "bilateral"
  | "conditional"
  | "website_public"
  | "website_private"
  | "arbiter_only";

type LayerEfficiency =
  | "native"       // +25-50% generation, -1 action cost
  | "efficient"    // standard
  | "weak"         // reduced generation, +1 action cost
  | "hostile";     // minimal generation, +1-2 action cost

type DistrictType =
  | "transit_hub"
  | "commercial_strip"
  | "residential_zone"
  | "media_district"
  | "harbor_freight"
  | "university_perimeter"
  | "industrial_fringe"
  | "data_exchange"
  | "financial_clearinghouse"
  | "power_grid"
  | "communications_hub"
  | "civic_administration"
  | "medical_complex"
  | "transit_control"
  | "corporate_campus"
  | "research_facility"
  | "government_citadel"
  | "military_installation"
  | "intelligence_hq"
  | "financial_sanctum"
  | "corporate_tower"
  | "chorus_research"
  | "chorus_node";

type DevelopmentGeneration = 0 | 1 | 2 | 3 | 4 | 5;

type BleedPropagationChannel =
  | "physical"
  | "social"
  | "informational"
  | "digital";

type BleedEffectType =
  | "security_level_modifier"
  | "action_cost_modifier"
  | "action_success_modifier"
  | "asset_loyalty_modifier"
  | "recruitment_modifier"
  | "intelligence_generation_modifier"
  | "resource_generation_modifier"
  | "propaganda_effectiveness_modifier"
  | "detection_modifier"
  | "structure_damage"
  | "digital_access_modifier"
  | "popularity_modifier"
  | "stability_modifier";

// ============================================
// AUDIO SYSTEM
// ============================================

type SoundtrackPhase =
  | "upkeep" | "placement" | "private_actions"
  | "public_actions" | "resolution" | "debrief"
  | "scoring" | "session_opening" | "session_closing"
  | "idle";

interface SoundtrackParameters {
  tension: number;           // 0.0-1.0
  complexity: number;        // 0.0-1.0
  chorusPresence: number;    // 0.0-1.0
  portraitQuality: PortraitQuality;
  currentPhase: SoundtrackPhase;
  roundNumber: number;
  activeConflicts: number;
  arbiterStage: 1 | 2 | 3 | 4 | 5;
}

interface AudioCue {
  cueId: AudioCueID;
  type: string;
  triggerEvent: string;
  audioFile: string;
  generatedScript?: string;
  duration: number;          // milliseconds
  volume: number;            // 0.0-1.0
  ducksSoundtrack: boolean;
  duckLevel: number;
  priority: number;
  isVoiced: boolean;
  hapticPattern?: HapticPattern;
}

interface HapticPattern {
  pulses: HapticPulse[];
  targetScope: "all" | "faction" | "player";
  targetId?: string;
}

interface HapticPulse {
  durationMs: number;
  intensityPercent: number;  // 0-100
  pauseAfterMs: number;
}

interface AudioState {
  soundtrackActive: boolean;
  currentSoundtrackParams: SoundtrackParameters;
  soundtrackVolume: number;
  masterVolume: number;
  activeCues: ActiveAudioCue[];
  queuedCues: AudioCue[];
  voiceEnabled: boolean;
  voiceGenerationMethod: "api" | "pregenerated" | "hybrid";
  pendingVoiceLines: PendingVoiceLine[];
  lastVoiceTimestamp: number;
  speakerConnected: boolean;
  amplifierInitialized: boolean;
}

interface ActiveAudioCue {
  cue: AudioCue;
  startedAt: number;
  expectedEndAt: number;
  canInterrupt: boolean;
}

interface PendingVoiceLine {
  script: string;
  priority: number;
  triggeredBy: string;
  requestedAt: number;
  isGenerated: boolean;
  audioFile: string | null;
}

// ============================================
// TIMING SYSTEM
// ============================================

interface PhaseTimer {
  phaseType: PhaseType;
  maxDurationSeconds: number;
  startedAt: number;
  expiresAt: number;
  autoExpiryEnabled: boolean;
  autoExpiryCondition: AutoExpiryCondition;
  playerReadyStates: Record<PlayerID, PlayerReadyState>;
  isExpired: boolean;
  expiredAt: number | null;
  expiredBy: "timer" | "all_ready" | "manual";
  warningThresholds: TimerWarning[];
}

interface AutoExpiryCondition {
  type:
    | "all_submitted"
    | "all_declared"
    | "all_placed"
    | "all_ready"
    | "majority_voted"
    | "never";
  additionalDelaySeconds: number;
}

interface PlayerReadyState {
  playerId: PlayerID;
  actionsAllocated: number;
  actionsSubmitted: number;
  explicitlyDone: boolean;
  readyAt: number | null;
}

interface TimerWarning {
  secondsRemaining: number;
  audioTriggered: boolean;
  hapticTriggered: boolean;
  displayUpdate: string;
}

// ============================================
// RESOURCE SYSTEM
// ============================================

interface ResourcePool {
  capital: number;
  infrastructure: number;
  signal: number;
  intelligence: number;
  influenceOperational: number;
  influencePublic: number;
}

interface ConversionRecord {
  conversionId: string;
  timestamp: number;
  fromResource: ResourceType;
  fromAmount: number;
  toResource: ResourceType;
  toAmount: number;
  conversionType:
    | "arbiter_4to1"
    | "signal_5to1"
    | "oi_to_pi"
    | "pi_to_oi"
    | "asset_liquidation"
    | "decay";
  publiclyNotified: boolean;
}

interface TradeRecord {
  tradeId: string;
  timestamp: number;
  roundId: RoundID;
  phaseType: PhaseType;
  party1: FactionID;
  party2: FactionID;
  party1Gives: Partial<ResourcePool>;
  party2Gives: Partial<ResourcePool>;
  cardsExchanged: CardTrade[];
  isPublic: boolean;
}

interface CardTrade {
  cardId: CardID;
  fromFaction: FactionID;
  toFaction: FactionID;
  loyaltyRevealedToReceiver: boolean;
}

// ============================================
// PLAYER AND OPERATOR
// ============================================

interface PlayerProfile {
  playerId: PlayerID;
  handle: string;
  nfcTokenIds: string[];
  cipherHash: string;
  registeredDeviceIds: string[];
  covenantHistory: CovenantID[];
  createdAt: number;
  lastSeenAt: number;
  totalSessionsPlayed: number;
}

interface OperatorDefinition {
  operatorId: OperatorID;
  factionId: FactionID;
  name: string;
  biographyNarrative: string;
  passiveAbilityId: string;
  passiveAbilityNarrative: string;
  activeAbilityId: string;
  activeAbilityCost: Partial<ResourcePool>;
  activeAbilityNarrative: string;
  unlockConditions: {
    awakening: UnlockCondition;
    ascendant: UnlockCondition;
    apex: UnlockCondition;
  };
  unlockAbilities: {
    awakening: UnlockAbility;
    ascendant: UnlockAbility;
    apex: UnlockAbility;
  };
  hiddenAgendaPool: HiddenAgendaDefinition[];
  doctrineAlignmentMap: Record<ActionType, DoctrineAlignment>;
}

interface UnlockCondition {
  conditionId: string;
  description: string;           // arbiter_only
  checkFunction: string;
  resetBetweenSessions: boolean;
  cumulativeAcrossSessions: boolean;
  progressNotificationThresholds: number[];
}

interface UnlockAbility {
  abilityId: string;
  name: string;
  narrativeDescription: string;
  cost: Partial<ResourcePool>;
  apexCostNonNativeRequired: Partial<ResourcePool>;
}

interface HiddenAgendaDefinition {
  agendaId: string;
  tier: "simple" | "moderate" | "complex";
  narrativeDescription: string;
  checkFunction: string;
  vpValue: number;
}

// ============================================
// SESSION PARTICIPANT
// ============================================

interface SessionParticipant {
  playerId: PlayerID;
  factionId: FactionID;
  operatorId: OperatorID;
  role: "director" | "operative" | "analyst" | "broker";

  // Action economy
  actionsPerRound: number;
  // Single player: 4
  // 2 players same faction: 3
  // 3+ players same faction: 2
  // Hard cap: 8 per faction total
  freeOperativeActionsPerRound: 1;

  // Hidden (arbiter_only)
  assignedAgendaId: string;
  agendaProgress: number;
  agendaMet: boolean;
  unlocksAchieved: UnlockTier[];
  unlockProgress: {
    awakening: number;
    ascendant: number;
    apex: number;
  };

  operatorPubliclyRevealed: boolean;
  revealedAtRound: number | null;
  complexityTier: "initiate" | "operative" | "veteran";

  joinedAtRound: number;
  joinType: "start" | "mid_session" | "returning";
  isPresent: boolean;
  isConnected: boolean;
  lastActiveAt: number;

  seatIndex: number | null;
  terminalId: string | null;

  currentRoundActionsSubmitted: number;
  currentRoundDeclaredDone: boolean;
}

// ============================================
// FACTION STATE
// ============================================

interface FactionState {
  factionId: FactionID;
  controlType: "human" | "ambient_power" | "arbiter_direct";
  ambientPowerTier: AmbientPowerTier | null;
  participants: PlayerID[];

  resources: {
    declared: ResourcePool;      // public [declared narrative]
    actual: ResourcePool;        // faction_only
    shadow: ResourcePool;        // arbiter_only
    assetPoints: number;
  };

  conversionHistory: ConversionRecord[];
  tradeHistory: TradeRecord[];

  influenceOI: number;           // faction_only
  influencePI: number;           // faction_only
  popularityState: PopularityState; // public
  popularityHistory: PopularityEvent[];

  doctrineId: string;            // faction_only
  doctrineAlignmentScore: number; // arbiter_only
  portraitScore: number;         // arbiter_only
  portraitContributions: PortraitContribution[];

  resonanceContribution: number; // arbiter_only
  activeEffects: ActiveEffect[];

  publicVP: number;              // public
  hiddenVP: number;              // arbiter_only
}

interface PopularityEvent {
  roundId: RoundID;
  change: number;
  cause: string;
  visibility: VisibilityScope;
}

interface PortraitContribution {
  roundId: RoundID;
  actionId: ActionID;
  alignment: DoctrineAlignment;
  magnitude: number;
  narrativeNote: string;
  visibility: "arbiter_only";
}

interface ActiveEffect {
  effectId: string;
  type: string;
  sourceActionId: ActionID;
  sourceFactionId: FactionID;
  roundsRemaining: number;
  parameters: Record<string, unknown>;
  visibility: VisibilityScope;
}

// ============================================
// HEX DISTRICT STATE
// ============================================

interface HexState {
  hexId: HexID;
  coordinate: HexCoordinate;
  districtName: string;
  districtType: DistrictType;
  historicalData: DistrictHistoricalData;

  layerControl: Record<Layer, LayerControlState>;

  structures: Structure[];
  hiddenStructures: Structure[];

  physicalSecurityLevel: number;  // public
  digitalSecurityLevel: number;   // arbiter_only

  tokenPresence: TokenPresence[];
  isContested: boolean;
  contestingFactions: FactionID[];

  activeOperations: ActiveOperation[];
  incomingBleedEffects: BleedEffect[];
  outgoingBleedEffects: BleedEffect[];
  connectivity: HexConnectivity;

  controlHistory: ControlHistoryEntry[];
  activeIncompatibilities: Incompatibility[];
  currentGenerationRates: Record<FactionID, Partial<ResourcePool>>;
}

interface HexCoordinate {
  ring: "sprawl" | "infrastructure" | "core" | "center";
  position: number;
  id: HexID;
}

interface DistrictHistoricalData {
  developmentGeneration: DevelopmentGeneration;
  establishedYear: number;
  historicalNarrative: string;
  architecturalCharacter: string;
  originalPurpose: string;
  currentPurpose: string;
}

interface LayerControlState {
  layer: Layer;
  controllingFaction: FactionID | null;
  controlEffectiveness: EffectivenessLevel;
  controlDuration: number;
  isHidden: boolean;
  hiddenFrom: FactionID[];
  resourceGeneration: Partial<ResourcePool>;
  layerEfficiency: LayerEfficiency;
}

interface Structure {
  structureId: string;
  factionId: FactionID;
  type: "basic" | "fortified" | "hidden" | "monument";
  layer: Layer;
  health: number;
  installedAtRound: number;
  isHidden: boolean;
  hiddenFrom: FactionID[];
}

interface TokenPresence {
  factionId: FactionID;
  tokenId: string;
  placedAtTimestamp: number;
  effectiveness: EffectivenessLevel;  // faction_only
}

interface ActiveOperation {
  operationId: string;
  factionId: FactionID;
  operationType: ActionType;
  targetLayer: Layer;
  roundStarted: number;
  roundsRemaining: number | null;
  visibility: VisibilityScope;
  parameters: Record<string, unknown>;
}

interface BleedEffect {
  effectId: BleedEffectID;
  sourceHexId: HexID;
  sourceEventType: string;
  sourceActionId: ActionID | null;
  sourceFactionId: FactionID | null;
  propagationChannel: BleedPropagationChannel;
  affectedLayer: Layer | "all";
  effectType: BleedEffectType;
  magnitude: number;
  roundsRemaining: number;
  roundCreated: number;
  visibility: VisibilityScope;
  narrativeDescription: string;
  affectedHexIds: HexID[];
}

interface HexConnectivity {
  hexId: HexID;
  adjacentHexIds: HexID[];
  infrastructureConnectedHexIds: HexID[];
  socialNetworkConnectedHexIds: HexID[];
  powerGridConnected: boolean;
}

interface ControlHistoryEntry {
  roundId: RoundID;
  layer: Layer;
  faction: FactionID | null;
  changeType: "claimed" | "lost" | "contested" | "transferred" | "shared";
}

interface Incompatibility {
  actionType: ActionType;
  consequence: string;
  popularityCost: number;
  stabilityImpact: number;
}

// ============================================
// ASSET SYSTEM
// ============================================

type AssetCapabilityType =
  | "access" | "intelligence_gen" | "cover"
  | "technical" | "financial" | "social"
  | "security" | "political" | "research";

interface AssetInstance {
  assetId: AssetID;
  cardId: CardID;
  controllingFaction: FactionID;
  custodyHistory: CustodyRecord[];

  homeHexId: HexID;
  currentHexId: HexID;

  loyalty: LoyaltyLevel;         // arbiter_only (hint to owner)
  loyaltyValue: number;          // arbiter_only
  exposure: ExposureLevel;       // arbiter_only
  isBurned: boolean;

  capabilityType: AssetCapabilityType;
  capabilityResourceType: ResourceType;
  passiveGenerationAmount: number;
  activeActionCost: Partial<ResourcePool>;

  isOccupied: boolean;
  occupiedUntilRound: number;
  activatedThisRound: boolean;
  lastActivatedRound: number;

  networkContacts: NetworkContact[];    // arbiter_only
  approachAttempts: ApproachAttempt[]; // arbiter_only
}

interface NetworkContact {
  contactName: string;
  role: string;
  hexId: HexID;
  isReachableThrough: AssetID;
}

interface ApproachAttempt {
  roundId: RoundID;
  byFaction: FactionID;
  approach: "direct" | "network";
  outcome: "failed" | "partial" | "succeeded" | "reported";
  loyaltyImpact: number;
}

interface CustodyRecord {
  fromFaction: FactionID | null;
  toFaction: FactionID;
  transferredAtRound: number;
  transferMethod: "accord" | "theft" | "defection" | "arbiter" | "trade";
}

// ============================================
// CARD SYSTEM
// ============================================

interface CardInstance {
  cardId: CardID;
  cardType: CardType;
  nfcId: string;
  qrCode: string;

  assignedRole: CardAssignment | null;
  currentHolder: PlayerID | FactionID | "burned_pile" |
                 "seized_pile" | "arbiter_archive" | "unassigned";
  custodyHistory: CardCustodyRecord[];

  isActive: boolean;
  isExpired: boolean;
  expiresAtRound: number | null;
  ageInRounds: number;

  loyaltyRevealedToCurrentHolder: boolean;
  isCompromised: boolean;        // arbiter_only
  compromisedBy: FactionID | null;

  markStickers: MarkSticker[];
  covenantHistory: CovenantCardHistory[];
}

interface CardAssignment {
  assignedAt: number;
  covenantId: CovenantID;
  sessionId: SessionID;
  assignedRole: string;
  narrativeDescription: string;
  mechanicalEffect: CardMechanicalEffect;
  factionSpecificEffects: Partial<Record<FactionID, CardMechanicalEffect>>;
}

interface CardMechanicalEffect {
  effectType: string;
  parameters: Record<string, unknown>;
}

interface CardCustodyRecord {
  holder: string;
  acquiredAt: number;
  acquiredBy: string;
  releasedAt: number | null;
  releasedBy: string | null;
}

interface MarkSticker {
  color: "gold" | "red" | "blue" | "black";
  appliedAtSession: SessionID;
  reason: string;                // arbiter_only
}

interface CovenantCardHistory {
  covenantId: CovenantID;
  assignedRole: string;
  holder: string;
  notable: boolean;
  narrativeNote: string;
}

// ============================================
// ACCORD SYSTEM
// ============================================

interface AccordInstance {
  accordId: AccordID;
  type: "signal" | "accord" | "covenant_bond";
  parties: FactionID[];
  registeredAtRound: number;
  expiresAtRound: number | null;
  terms: AccordTerm[];
  hiddenClauses: AccordTerm[];   // arbiter_only (Negotiator)
  isActive: boolean;
  isHonored: boolean;
  isPubliclyDeclared: boolean;
  breachHistory: AccordBreach[];
}

interface AccordTerm {
  termId: string;
  type: string;
  description: string;
  mechanicalEffect: string;
  beneficiary: FactionID;
  isHidden: boolean;
}

interface AccordBreach {
  breachedBy: FactionID;
  breachedAtRound: number;
  termsBreached: string[];
  resourceConsequence: Partial<ResourcePool>;
  notifiedParties: FactionID[];
  wardenNotified: boolean;
}

// ============================================
// ACTION SYSTEM
// ============================================

interface ActionSubmission {
  actionId: ActionID;
  submittedBy: PlayerID;
  factionId: FactionID;
  actionType: ActionType;
  phase: PhaseType;
  roundId: RoundID;
  submittedAt: number;
  isPublic: boolean;

  parameters: ActionParameters;

  status: "pending" | "processing" | "resolved" |
          "failed" | "countered" | "cancelled" | "auto_passed";
  resolvedAt: number | null;
  outcome: ActionOutcome | null;

  portraitImpact: {
    factionId: FactionID;
    alignment: DoctrineAlignment;
    magnitude: number;
  } | null;                      // arbiter_only

  generatesBleedEffect: boolean;
  bleedEffectId: BleedEffectID | null;
}

interface ActionParameters {
  targetHexId?: HexID;
  targetLayer?: Layer;
  targetFactionId?: FactionID;
  targetPlayerId?: PlayerID;
  targetCardId?: CardID;
  targetAssetId?: AssetID;
  targetAccordId?: AccordID;
  resourceCommitment?: Partial<ResourcePool>;
  messageContent?: string;
  messageRecipients?: PlayerID[];
  isEncrypted?: boolean;
  abilityId?: string;
  cardId?: CardID;
  activationHexId?: HexID;
  assetId?: AssetID;
  assetAction?: string;
  questionText?: string;
  questionVote?: ActionID;
  broadcastContent?: string;
  broadcastType?: "alliance" | "denunciation" | "position" | "general";
  tradePartner?: FactionID;
  tradeGive?: Partial<ResourcePool>;
  tradeReceive?: Partial<ResourcePool>;
  tradeCards?: CardTrade[];
  conversionFromType?: ResourceType;
  conversionFromAmount?: number;
  conversionToType?: ResourceType;
  liquidateAssetId?: AssetID;
}

interface ActionOutcome {
  success: boolean;
  partial: boolean;
  effects: StateChange[];
  narrativeDescription: string;
  visibleToFactions: FactionID[];
  publicDescription: string | null;
  portraitNote: string | null;   // arbiter_only
  generatedAudioCue: AudioCueID | null;
  generatedBleedEffects: BleedEffectID[];
}

// ============================================
// STATE CHANGE EVENT SYSTEM
// ============================================

interface StateChange {
  changeId: string;
  timestamp: number;
  roundId: RoundID;
  phaseId: PhaseType;
  causedByActionId: ActionID | null;
  causedByBleedId: BleedEffectID | null;
  changeType: StateChangeType;
  payload: unknown;
  visibility: VisibilityScope;
  isReversible: boolean;
  isAdministrative: boolean;
  audioTriggered: AudioCueID | null;
}

type StateChangeType =
  | "resource_delta"
  | "resource_conversion"
  | "resource_trade"
  | "layer_control_change"
  | "popularity_change"
  | "oi_pi_conversion"
  | "asset_loyalty_change"
  | "asset_exposure_change"
  | "asset_burned"
  | "asset_defected"
  | "asset_occupied"
  | "asset_freed"
  | "structure_placed"
  | "structure_damaged"
  | "structure_destroyed"
  | "accord_registered"
  | "accord_breached"
  | "accord_expired"
  | "card_custody_change"
  | "card_activated"
  | "card_expired"
  | "card_compromised"
  | "unlock_achieved"
  | "agenda_progress"
  | "agenda_met"
  | "portrait_contribution"
  | "resonance_change"
  | "world_condition_change"
  | "chorus_layer_revealed"
  | "bleed_effect_created"
  | "bleed_effect_expired"
  | "bleed_effect_propagated"
  | "player_joined"
  | "player_departed"
  | "player_reconnected"
  | "ambient_power_action"
  | "phase_transition"
  | "timer_expired"
  | "timer_early_close"
  | "founding_figure_created"
  | "administrative_correction"
  | "audio_cue_triggered"
  | "soundtrack_parameter_change";

// ============================================
// TABLE QUESTION SYSTEM
// ============================================

interface TableQuestionState {
  resonanceValue: number;        // arbiter_only
  resonanceThreshold: number;    // arbiter_only
  windowIsOpen: boolean;         // public
  windowOpenedAt: number | null;
  windowTimer: PhaseTimer | null;
  currentProposals: QuestionProposal[];
  votingComplete: boolean;
  allPlayersVoted: boolean;
  selectedQuestion: string | null;
  arbiterResponse: string | null;
  arbiterResponseVoiced: boolean;
  questionsAskedThisSession: number;
  previousQuestions: PreviousQuestion[];
}

interface QuestionProposal {
  proposalId: string;
  proposedBy: PlayerID;          // arbiter_only
  questionText: string;
  votes: PlayerID[];             // count public, attribution arbiter_only
  currentVoteCount: number;      // public
  timestamp: number;
}

interface PreviousQuestion {
  roundId: RoundID;
  questionText: string;
  proposedBy: PlayerID;          // arbiter_only
  voteCount: number;
  wasUnanimous: boolean;
  dissenterCount: number;
  arbiterResponse: string;
  arbiterResponseType: "observation" | "reckoning" | "record" | "question_returned";
  wasVoiced: boolean;
}

// ============================================
// ROUND STATE
// ============================================

interface RoundState {
  roundId: RoundID;
  roundNumber: number;
  sessionId: SessionID;

  currentPhase: PhaseType;
  phaseHistory: PhaseTransition[];
  currentPhaseTimer: PhaseTimer | null;

  placementOrder: FactionID[];
  placementOrderRationale: string;
  placementsComplete: FactionID[];
  tokensPlacedThisRound: Record<FactionID, number>;

  privateActionTracking: Record<PlayerID, PlayerReadyState>;
  allPrivateActionsIn: boolean;
  privateActionsClosedBy: "timer" | "all_submitted" | null;

  publicActionTracking: Record<FactionID, boolean>;
  allPublicActionsDeclared: boolean;

  debriefReadyTracking: Record<PlayerID, boolean>;
  allPlayersReadyForNext: boolean;

  eventCardId: CardID | null;
  eventCardRevealed: boolean;
  eventCardNarrative: string | null;   // public
  eventCardEffect: string | null;      // arbiter_only
  eventCardAudioCue: AudioCueID | null;

  resolutionQueue: ActionID[];
  resolutionPriorityOrder: ActionID[][];
  resolutionComplete: boolean;

  questionState: TableQuestionState;
  bleedEffectsCreated: BleedEffectID[];

  soundtrackParamsThisRound: SoundtrackParameters;
  audioCuesThisRound: AudioCueID[];

  chorusActivityDelta: number;
  worldConditionDeltas: Partial<WorldConditions>;

  arbitratorNotes: ArbitratorNote[];   // arbiter_only
}

interface PhaseTransition {
  from: PhaseType;
  to: PhaseType;
  timestamp: number;
  triggeredBy: "timer" | "all_ready" | "arbiter" | "manual";
  audioCueTriggered: AudioCueID | null;
}

interface ArbitratorNote {
  noteId: string;
  category: "portrait" | "pattern" | "significant" | "reckoning" |
            "audio_trigger" | "founding_figure";
  content: string;
  relatedFactions: FactionID[];
  relatedActions: ActionID[];
  timestamp: number;
  shouldVoice: boolean;
  voicingPriority: number;
}

// ============================================
// WORLD CONDITIONS
// ============================================

interface WorldConditions {
  disclosure: number;
  consensus: number;
  stability: number;
  chorusActivity: number;
  arbiterTrust: number;
  portrait: number;

  disclosureNarrative: string;
  consensusNarrative: string;
  stabilityNarrative: string;
  chorusNarrative: string;
  trustNarrative: string;
  portraitNarrative: PortraitQuality;

  history: WorldConditionHistory[];
}

interface WorldConditionHistory {
  sessionId: SessionID;
  roundId: RoundID;
  track: string;
  delta: number;
  cause: string;
  causingFaction: FactionID | null;
}

// ============================================
// ARBITER INTERNAL STATE
// ============================================

interface ArbiterSessionState {
  currentStage: 1 | 2 | 3 | 4 | 5;
  resonanceValue: number;
  resonanceHistory: ResonanceEvent[];
  chorusKnowledge: ChorusKnowledge;
  observedPatterns: ObservedPattern[];
  pendingReckonings: PendingReckoning[];

  terminalLEDStates: Record<string, LEDState>;
  arbitratorRingState: LEDState;
  pulseRateMultiplier: number;

  currentSoundtrackParams: SoundtrackParameters;
  pendingAudioCues: AudioCue[];
  voiceGenerationQueue: PendingVoiceLine[];

  narrativeContext: NarrativeContext;
  administrativeActions: AdminAction[];
}

interface ChorusKnowledge {
  layersDecoded: number;
  resonanceActive: boolean;
  patternClassification: string;
  lastResonanceTimestamp: number;
}

interface ObservedPattern {
  patternId: string;
  description: string;
  involvedFactions: FactionID[];
  roundsObserved: number[];
  significance: "low" | "medium" | "high" | "critical";
  hasSurfacedToPlayers: boolean;
  narrativeTreatment: string;
}

interface PendingReckoning {
  targetPlayer: PlayerID;
  content: string;
  trigger: string;
  priority: number;
  expiresAtRound: number | null;
  shouldVoice: boolean;
  hapticPattern: HapticPattern;
}

interface ResonanceEvent {
  roundId: RoundID;
  delta: number;
  cause: string;
  causedByAction: ActionID | null;
}

interface LEDState {
  pattern: "pulse" | "steady" | "sweep" | "breathe" |
           "flash" | "cascade" | "off";
  color: string;
  speed: number;
  brightness: number;
  targetLeds?: number[];
}

interface NarrativeContext {
  currentStage: number;
  portraitQuality: PortraitQuality;
  dominantFaction: FactionID | null;
  sessionTension: "low" | "medium" | "high" | "critical";
  notableEvents: string[];
  arbiterMood: string;
  roundNumber: number;
  worldConditionSummary: string;
  activeFoundingFigures: string[];
  recentNarrativeEvents: string[];
  soundtrackTension: number;
}

interface AdminAction {
  adminActionId: string;
  performedAt: number;
  actionType: string;
  description: string;
  stateChangesApplied: string[];
  narrativeDelivered: string | null;
  audioTriggered: boolean;
}

// ============================================
// SESSION STATE
// ============================================

interface SessionState {
  sessionId: SessionID;
  covenantId: CovenantID;
  sessionNumber: number;

  playMode: PlayMode;
  difficulty: "cautious" | "measured" | "decisive" | "relentless";
  startedAt: number;
  endedAt: number | null;

  participants: SessionParticipant[];
  seatMap: TableSeat[];
  cooperativeFactionGroups: Record<FactionID, PlayerID[]>;

  factionStates: Record<FactionID, FactionState>;
  hexStates: Record<HexID, HexState>;
  activeBleedEffects: Record<BleedEffectID, BleedEffect>;
  assets: Record<AssetID, AssetInstance>;
  activeCards: Record<CardID, CardInstance>;
  accords: Record<AccordID, AccordInstance>;

  currentRound: RoundState;
  completedRounds: RoundID[];
  allRounds: Record<RoundID, RoundState>;

  actionHistory: ActionSubmission[];
  eventLog: StateChange[];

  worldConditions: WorldConditions;
  audioState: AudioState;
  arbiterState: ArbiterSessionState;

  chronicleInProgress: string;
}

interface TableSeat {
  seatIndex: number;
  detectedPosition: { x: number; y: number; confidence: number };
  playerId: PlayerID | null;
  terminalId: string | null;
  lastSeenTimestamp: number;
  detectionMethod: "nfc_auth" | "cv_terminal" | "wifi_rssi" |
                   "face_detect" | "self_declared";
}

// ============================================
// COVENANT STATE
// ============================================

interface CovenantState {
  covenantId: CovenantID;
  covenantNumber: number;
  startedAt: number;
  endedAt: number | null;
  endCondition: "response_sent" | "table_collapsed" |
                "revelation" | "in_progress" | null;

  sessions: SessionID[];
  currentSession: SessionID | null;

  worldConditions: WorldConditions;
  operatorLegacy: Record<OperatorID, OperatorLegacyState>;

  portraitScore: number;
  portraitHistory: PortraitHistoryEntry[];
  portraitNarrative: string;

  cardAssignments: Record<CardID, CardAssignment>;
  foundingFigures: FoundingFigure[];

  arbiterStage: 1 | 2 | 3 | 4 | 5;
  arbiterEvolutionNotes: string[];
  signatureAudioMoments: SignatureAudioMoment[];

  accountingDocument: string | null;
}

interface FoundingFigure {
  operatorId: OperatorID;
  operativeName: string;
  faction: FactionID;
  roleType: string;
  fromCovenantId: CovenantID;
  fromSessionId: SessionID;
  fromRound: number;

  apexAbilityUsed: string;
  apexNarrative: string;
  apexSucceeded: boolean;        // REQUIRED — must succeed
  portraitContribution: number;

  permanentRecord: string;
  physicalCardStamped: boolean;

  successorBriefing: string;
  worldPresence: string;
  audioCueId: AudioCueID | null;
}

interface SignatureAudioMoment {
  momentId: string;
  sessionId: SessionID;
  roundId: RoundID;
  description: string;
  audioFiles: string[];
  narrativeContext: string;
}

interface OperatorLegacyState {
  operatorId: OperatorID;
  operativeName: string;
  legacyEvents: LegacyEvent[];
  currentStatus: "active" | "scarred" | "defected" |
                 "disappeared" | "turned" | "founding_figure";
  scars: Scar[];
  ascensionAchieved: boolean;
  apexUsedCount: number;
  apexSuccessCount: number;
  isFoundingFigure: boolean;
  foundingFigureId: string | null;
}

interface LegacyEvent {
  eventType: "ascension" | "scar" | "defection" |
             "disappearance" | "the_turn" | "return" |
             "founding_figure";
  sessionId: SessionID;
  roundId: RoundID;
  narrative: string;
  mechanicalEffect: string;
  legacyCardId: CardID | null;
  audioCueTriggered: AudioCueID | null;
}

interface Scar {
  scarId: string;
  description: string;           // faction visibility
  mechanicalEffect: string;      // arbiter_only
  acquiredAt: SessionID;
  isActive: boolean;
}

interface PortraitHistoryEntry {
  sessionId: SessionID;
  contribution: number;
  narrativeNote: string;
  dominantQuality: string;
}

// ============================================
// HARDWARE STATE
// ============================================

interface HardwareState {
  terminals: Record<string, TerminalState>;
  arbiterUnit: ArbiterUnitState;
  projector: ProjectorState;
  camera: CameraState;
  audio: AudioHardwareState;
}

interface TerminalState {
  terminalId: string;
  assignedPlayerId: PlayerID | null;
  firmwareVersion: string;
  isConnected: boolean;
  lastHeartbeat: number;
  batteryLevel: number;
  ledState: Record<string, LEDState>;
  currentScreen: string;
  hapticMotorAvailable: boolean;
  speakerAvailable: false;       // terminals have NO speaker
}

interface ArbiterUnitState {
  isOnline: boolean;
  firmwareVersion: string;
  ringLEDState: LEDState;
  sessionMode: "administrative" | "session" | "idle" | "standby";
  adminKeyInserted: boolean;
  audioEnabled: boolean;
  currentVolume: number;
}

interface AudioHardwareState {
  speakerConnected: boolean;
  amplifierInitialized: boolean;
  currentOutputLevel: number;
  masterVolume: number;
  soundtrackActive: boolean;
  activeCueCount: number;
  voiceGenerationAvailable: boolean;
  voiceApiStatus: "available" | "degraded" | "unavailable";
  preGeneratedLibraryLoaded: boolean;
  preGeneratedCueCount: number;
}

interface ProjectorState {
  isActive: boolean;
  calibrationValid: boolean;
  lastCalibrationAt: number;
  currentProjection: string;
  brightness: number;
}

interface CameraState {
  isActive: boolean;
  lastFrameAt: number;
  detectedTokens: DetectedToken[];
  detectedTerminals: DetectedTerminal[];
  calibrationValid: boolean;
  irIlluminationActive: boolean;
}

interface DetectedToken {
  arucoId: number;
  factionId: FactionID;
  hexId: HexID | null;
  position: { x: number; y: number };
  confidence: number;
  lastSeenAt: number;
}

interface DetectedTerminal {
  terminalId: string | null;
  position: { x: number; y: number };
  seatIndex: number | null;
  factionColor: string;
  confidence: number;
}

// ============================================
// SYSTEM STATE
// ============================================

interface SystemState {
  serverVersion: string;
  databaseVersion: string;
  claudeApiStatus: "available" | "degraded" | "unavailable";
  claudeApiLatencyMs: number;
  lastApiCallAt: number;
  audioApiStatus: "available" | "degraded" | "unavailable";
  pendingOTAUpdate: string | null;
  websiteLastSyncAt: number;
  activeConnections: number;
  errorLog: SystemError[];
}

interface SystemError {
  errorId: string;
  timestamp: number;
  severity: "info" | "warning" | "error" | "critical";
  component: string;
  message: string;
  resolved: boolean;
}

// ============================================
// ROOT GAME STATE
// ============================================

interface GameState {
  schemaVersion: string;          // "0.2.0"
  gameId: string;
  createdAt: number;
  lastModifiedAt: number;

  covenants: Record<CovenantID, CovenantState>;
  currentCovenant: CovenantID | null;
  currentSession: SessionState | null;

  players: Record<PlayerID, PlayerProfile>;
  cardRegistry: Record<CardID, CardInstance>;
  operatorDefinitions: Record<OperatorID, OperatorDefinition>;

  hardware: HardwareState;
  systemState: SystemState;
  audioState: AudioState;
}
```

---

## Schema Change Log

### v0.1 → v0.2

**Action Economy**
- `SessionParticipant.actionsPerRound`: computed value (4/3/2) based on cooperative player count
- Hard cap of 8 standard actions per faction regardless of player count

**Resources**
- Added `assetPoints` to `ResourcePool`
- Added `ConversionRecord`, `TradeRecord`, `CardTrade` types
- Added `ResourceDecayConfig` for Intelligence and Signal decay
- OI/PI split formalized in `FactionState`

**Audio System (new)**
- `SoundtrackParameters`, `AudioCue`, `HapticPattern`, `HapticPulse`
- `AudioState`, `AudioHardwareState`
- `AudioCueID` type added
- Audio fields added to `ArbiterSessionState`, `RoundState`, `ActionOutcome`, `StateChange`, `LegacyEvent`, `CovenantState`

**Timing System (new)**
- `PhaseTimer`, `AutoExpiryCondition`, `PlayerReadyState`, `TimerWarning`
- Per-player ready tracking in `RoundState`
- `declare_done` action type added
- `timer_expired`, `timer_early_close` state change types added

**City History (new)**
- `DevelopmentGeneration` type
- `DistrictHistoricalData` interface
- `HexState.historicalData` field

**Bleed-Over (formalized)**
- `BleedEffect`, `BleedPropagationChannel`, `BleedEffectType` types
- `HexConnectivity` interface
- `HexState.incomingBleedEffects`, `outgoingBleedEffects`, `connectivity`

**Founding Figures (revised)**
- `FoundingFigure.apexSucceeded` required field
- `FoundingFigure.successorBriefing` and `worldPresence` added
- `OperatorLegacyState.apexSuccessCount` added

**Hardware**
- `TerminalState.speakerAvailable: false` — explicit no-speaker constraint
- `AudioHardwareState` interface added

---
