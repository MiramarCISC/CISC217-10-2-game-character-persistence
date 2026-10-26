"""Database functions for the Week 10 SQL and SQLite lab."""


def create_schema(connection):
    """Create the character_types and characters tables."""
    raise NotImplementedError


def add_character_type(connection, name):
    """Insert one character type and return its new row id."""
    raise NotImplementedError


def add_character(connection, name, health, power, type_id=None):
    """Insert one character and return its new row id."""
    raise NotImplementedError


def get_character(connection, character_id):
    """Return (id, name, health, power, type_id), or None."""
    raise NotImplementedError


def list_characters(connection):
    """Return all characters ordered by id."""
    raise NotImplementedError


def strong_characters(connection, minimum_power):
    """Return characters with power >= minimum_power, highest first."""
    raise NotImplementedError


def list_characters_with_types(connection):
    """Use INNER JOIN and return (character_name, power, class_name)."""
    raise NotImplementedError


def list_all_characters_with_optional_types(connection):
    """Use LEFT JOIN and return (character_name, class_name)."""
    raise NotImplementedError


def update_health(connection, character_id, new_health):
    """Update health and return affected row count."""
    raise NotImplementedError


def delete_character(connection, character_id):
    """Delete by id and return affected row count."""
    raise NotImplementedError
