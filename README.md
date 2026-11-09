# Ashen Hollow Online

A browser-based multiplayer social deduction card game project focused on allowing friends to play remotely.

## Stack (planned)
- React + TypeScript + Phaser (2D client)
- Python + FastAPI + WebSockets (authoritative rules server)
- PostgreSQL later, for persistence

## Status
**Phase 1: rules/data foundation.** No full multiplayer gameplay has been implemented yet.

## Start here
- [Game Design Document](docs/game_design.md)
- [Working Gameplay Rules](docs/game_rules.md)
- [Technical Architecture](docs/architecture.md)
- [Character database](game_data/characters.json)
- [Preliminary Playing card database](game_data/playing_cards.json)
- [Tryal setup distribution](game_data/tryals.json)

## Verify reference data
From the project root:

```bash
python backend/tests/check_game_data.py
```

## Reference material and rights
Initial prototype uses Salem 1692 Standard / 2nd Edition rules as a research reference, along with a user-provided Town Hall ability image. This repository should use original or appropriately licensed artwork and game content for any public release. Do not commit copyrighted publisher rulebook PDFs/card assets without permission.
