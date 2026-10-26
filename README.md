# CISC 217 Week 10 — Game Character Persistence Lab

Build a small SQLite data-access module for game characters.

## You will practice

- SQLite tables and data types
- primary and foreign keys
- CRUD operations
- WHERE and ORDER BY
- parameterized queries
- INNER JOIN
- LEFT JOIN
- Python sqlite3
- cursors and query results
- in-memory SQLite testing

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[test]'
python -m pytest -q
```

## Required work

Complete the functions in:

```text
src/cisc217_week10/database.py
```

Functions:

- `create_schema()`
- `add_character_type()`
- `add_character()`
- `get_character()`
- `list_characters()`
- `strong_characters()`
- `list_characters_with_types()`
- `list_all_characters_with_optional_types()`
- `update_health()`
- `delete_character()`

## Rules

- Use Python's built-in `sqlite3` module.
- Use parameter placeholders for Python values.
- Do not build SQL with f-strings.
- Use `INNER JOIN` in `list_characters_with_types()`.
- Use `LEFT JOIN` in `list_all_characters_with_optional_types()`.
- Do not hard-code a database filename inside the database functions.
- Do not modify instructor tests just to make incorrect code pass.
