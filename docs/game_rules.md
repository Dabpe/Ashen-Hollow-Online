# Standard-Edition Gameplay Specification — Working Draft

**Status:** Reference-derived; not yet a complete implementable ruleset.  
**Priority:** Supplied Salem 1692 2nd Edition rulebook and user-provided character card image.  
**Excluded:** Deluxe-only rules.

## 1. Setup
- Player count: 4–12. See `game_data/tryals.json` for the reference Tryal allocation.
- Randomly give each player a Town Hall character face up. For 7 or fewer players, the source offers an optional choice from two dealt characters.
- Shuffle and deal Tryals face down, to be viewed privately by their owner. Witch allegiance persists if a Witch card is ever owned. Constable status follows current ownership of the Constable Tryal.
- Deal three Playing cards to each player. Shuffle Conspiracy into the draw deck; place Night at the bottom. Hold Black Cat aside until Dawn.
- Dawn: Witches identify one another and assign Black Cat (including to a Witch); Black Cat holder acts first, then clockwise.

## 2. Turn choices
Exactly one primary choice per turn:
- **Draw two** from deck and end the turn; a Black card immediately resolves when drawn and counts toward the two draws.
- **Play one or more** cards onto other players, resolving each. Green cards discard after use. Blue cards persist before a player until removed/moved, while Red cards accumulate accusations until a Tryal is revealed.

The standard first Law prohibits directly playing cards/Gavel on yourself. Source exceptions, such as the Witch choice of Black Cat during Dawn, must be coded explicitly.

## 3. Accusations / Tryal reveal
- Normally, seven total accusation points on a target cause one hidden Tryal to be revealed, selected by the player placing the final accusation; Red cards on that target are discarded afterward.
- Excess points do not roll over into the next Tryal reveal.
- Character and Blue-card effects can modify thresholds, values or protection; determine effective values from the active event context.
- A player dies if all Tryals have been revealed, if a revealed Tryal says Witch, or if the Night kill succeeds. Standard-source exceptions and character interactions must be checked before treating these as unqualified generic rules.

## 4. Conspiracy
A Conspiracy Black card resolves immediately:
1. If Black Cat is assigned, the player who drew Conspiracy reveals a hidden Tryal belonging to Black Cat holder (per source rules and exceptions).
2. Players simultaneously choose one unrevealed Tryal from the player on their left and add it to their own hidden set.
3. The recipient privately reviews the new set. Obtaining Witch makes a player permanently aligned with Witches. Losing it does not undo Witch allegiance.
4. Constable power changes with current possession of Constable Tryal.

**Implementation alert:** If the initial Black Cat reveal causes elimination or victory, check exact resolution ordering before implementing automatic transfers.

## 5. Night
When Night is drawn, the game temporarily suspends normal turn flow:
1. Living Witch-aligned players privately select an intended victim (the official rules assume in-person coordination).
2. Current Constable secretly assigns Gavel to any other living player.
3. Before the target is announced, eligible players may Confess by revealing a chosen own Tryal for Night-kill immunity.
4. Reveal the victim; protection from Gavel, Confession or Asylum prevents the Night kill; otherwise the chosen player dies and reveals remaining Tryals.
5. Shuffle discards into the deck, putting Night at the bottom again, and resume turn order where interrupted.

For the digital version, Witch target agreement and timeout treatment are application design decisions and must be documented separately.

## 6. Death and winning
- After death: discard hand and Blue cards; reveal all remaining Tryals. Standard rulebook also requires truthful declaration of whether the player ever owned a Witch Tryal.
- Townspeople win once all Witch **Tryal cards** have been revealed, not necessarily after eliminating all Witch-aligned players.
- Witches win when everyone still alive is Witch-aligned (currently or formerly owned a Witch card).
- Check victory in a deliberate event priority order; never expose private Tryals by broadcasting the full server state.

## 7. Special reference interactions
- Stocks: stay until the affected turn is skipped; multiple Stocks can stack.
- Matchmaker: two linked owners can both die on a Night kill; some edge cases in printed pages 10–11.
- Black Cat: treated as Blue card after Dawn and may be moved/removed; special Conspiracy interaction when holder draws Conspiracy.
- Blue cards are removed when only two players remain (source printed page 10).
- Scapegoat/Robbery cannot be arranged for direct self-benefit (printed page 11).
- See `game_data/characters.json` for each character's sourced reference effect.

## 8. Explicit unresolved rules
- Exact counts and printed texts for all Playing card types.
- Confirmation of Piety's exact card-front effect in this physical printing.
- Ability priority when multiple effects chain or trigger Black cards while resolving another action.
- Specific character edge cases not fully described on Town Hall image.
- Table consensus and turn-clock behavior in a remote browser game.

## Evidence map
- Printed pages 2–5: setup, Dawn and turns.
- Printed pages 6–7: victory, Conspiracy and laws.
- Printed pages 8–9: Night.
- Printed pages 10–11: special exceptions.
- User-provided image: 15 character texts.
