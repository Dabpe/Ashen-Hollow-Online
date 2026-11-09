# Technical Architecture — Proposed

## Frontend
React + TypeScript for lobby, authentication, HUD and accessibility. Phaser renders the game table, cards, and effects. React/Phaser exchange UI events through a bridge. The graphical layer never decides legality or outcomes.

## Transport
One WebSocket connection per player session to FastAPI. Messages carry `room_id`, `action_id`, action `type`, and payload. Responses have monotonically increasing `event_sequence` IDs. Reject duplicate action IDs and validate turn/state on the server.

## Backend
Pure Python rule handlers change a server-owned game state. A projection function builds **separate** public and per-player private views; never serialize the full server state to a player.

## Data
`game_data/*.json` provides versioned static definitions. Start with one in-memory room worker and no persistent games. Introduce PostgreSQL for accounts and save/recovery after core engine correctness.

## Testing
Unit tests for game transitions; property tests for card conservation and secret visibility; integration tests for two clients in the same room; browser end-to-end tests for reconnection and card animation triggers.

## Example command
```json
{"type":"PLAY_CARD","room_id":"ABCD12","action_id":"unique-id","payload":{"card_id":"instance-12","target_player_id":"p2"}}
```

## Example event
```json
{"event_sequence":42,"type":"CARD_PLAYED","actor_id":"p1","card_type":"accusation","target_player_id":"p2"}
```

**Security:** `action_id` is for deduplication, not authorization. Server authenticates the player session and checks ownership of card instances.
