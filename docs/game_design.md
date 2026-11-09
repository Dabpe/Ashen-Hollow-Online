# Ashen Hollow Online — Game Design Document (GDD)

**Version:** 0.1.0 (design foundation)  
**Game:** Browser-based social deduction card game  
**First rules reference:** Salem 1692, 2nd Edition / Standard variant  
**Scope:** Private gameplay prototype initially; public release requires original/licensed assets and review of content rights.

## 1. Problem and vision
Friends enjoy a physical social deduction game but cannot always meet. The product enables remote groups to play together through a browser, with private hidden information, real-time cards and smooth 2D animations.

## 2. Target experience
- 4–12 players for the rules-reference prototype.
- A host creates a room and shares a short join code.
- Each user plays on desktop or mobile browser; no installation required.
- Character cards are public, Tryal cards and hands are private, and game announcements are synchronized.
- Atmosphere: original colonial-gothic art, illustrated cards, card flips, table effects, and optional sound.
- Voice chat can initially be handled externally (e.g. a normal voice call); in-app voice is deferred.

## 3. Product principles
1. **Server-authoritative rules:** clients send commands, server validates and changes state.
2. **Information security:** each player receives only authorized hidden information.
3. **Reliable reconnection:** a returning player sees a fresh filtered snapshot.
4. **Deterministic actions:** each server event has a sequence ID; animations do not decide game outcomes.
5. **Rule traceability:** every mechanic records an edition/source and an unresolved status when needed.

## 4. Rules baseline
Standard Salem-like rules from the supplied **2nd Edition rulebook** and user-selected Online Station article. The Deluxe edition is explicitly **out of scope** for MVP (no Shillings, special Tryals, wooden-token system, 2–3-player ghosts, or early Night placement).

The gameplay outline is in `docs/game_rules.md`. Character reference data is in `game_data/characters.json` and preliminary playing-card reference data is in `game_data/playing_cards.json`.

## 5. Digital game flow
1. Lobby (host creates room; players join).
2. Setup (assign Town Hall character, secret Tryals, three-card hands and shuffled deck).
3. Dawn (Witches privately coordinate Black Cat placement; Black Cat recipient begins).
4. Turns (draw two or play one-or-more cards); resolve red/green/blue effects and forced black-card events.
5. Conspiracy as drawn (reveal Black Cat holder Tryal if applicable; reassign unrevealed Tryals).
6. Night as drawn (Witches choose target; Constable protects; confession opportunity; resolve elimination).
7. Victory check after relevant events. Repeat until win.

## 6. Main screens
- Home: create/join room.
- Lobby: roster, readiness, instructions, host controls.
- Private role screen: assigned Tryals and public character ability.
- Game table: other players, accusations, blue cards, draw/discard piles, own hand, event feed.
- Night: eligible role-specific interface, pending/revealed state, Confession action.
- Game over: winning faction and controlled postgame reveal.

## 7. Graphics and motion
**Frontend:** React + TypeScript for lobby/HUD, Phaser for card/table scene. Prototype effects: hover lift, card drag/placement, flip/reveal, Conspiracy exchange, Night fade, elimination and victory. Favor local animation over networked frame-by-frame updates.

## 8. Backend architecture
FastAPI WebSocket server and pure-Python game-rules package. Suggested modules: `GameState`, `Player`, `CardEngine`, `TryalEngine`, `IdentityEngine`, `NightEngine`, `VictoryEngine`, `EventQueue` and `PublicViewBuilder`. Database persistence is a later milestone.

## 9. MVP scope
- Join/create room, 4 players initially in testing.
- Character and Tryal setup; hidden information partition.
- Draw two, Accusation, Tryal reveal and win check.
- Two browser windows show synchronized public actions.

Expand after MVP to remaining action cards, Conspiracy, Night, character abilities, larger games and reconnect handling.

## 10. Open decisions
- Complete verified counts and printed effects of every Playing card.
- Standard-edition cards and character-specific priority/edge-case interactions.
- Timeout behavior and private Witch coordination interface.
- Exact process for source-consistent handling of revealing a card during effects and chained events.
- Public release licensing and original branding/content.

## Sources
- Supplied *FINAL_Salem_Rulebook_-2nd_Edition.pdf* (primary).
- User-provided 15 Town Hall character card image (ability reference).
- User-selected Online Station standard-edition article (secondary clarification).
- Deluxe rulebook is retained only for edition comparison; not the MVP baseline.
