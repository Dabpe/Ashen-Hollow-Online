"""Validate static card files without third-party dependencies.

Run at project root: python backend/tests/check_game_data.py
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]


def load_json(name):
    """Read a JSON database from game_data and return a Python dictionary."""
    path = ROOT / 'game_data' / name
    return json.loads(path.read_text(encoding='utf-8'))


def validate():
    """Check unique IDs and accounting invariants; raise on failures."""
    characters = load_json('characters.json')['characters']
    cards = load_json('playing_cards.json')['cards']
    tryals = load_json('tryals.json')['distribution']

    assert len(characters) == 15, 'Expected 15 Town Hall characters'
    assert len({c['id'] for c in characters}) == len(characters), 'Duplicate character IDs'
    assert len({c['id'] for c in cards}) == len(cards), 'Duplicate playing card IDs'
    assert {c['id'] for c in cards if c['color'] == 'black'} == {'night', 'conspiracy'}
    assert sorted(row['players'] for row in tryals) == list(range(4, 13))
    for row in tryals:
        total = row['not_a_witch'] + row['witch'] + row['constable']
        assert total == row['players'] * row['tryals_per_player'], row
    print(f"PASS: {len(characters)} characters, {len(cards)} reference card types, {len(tryals)} Tryal distributions")


if __name__ == '__main__':
    validate()
