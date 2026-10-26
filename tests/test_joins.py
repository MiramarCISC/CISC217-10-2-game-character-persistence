from cisc217_week10 import (
    add_character_type,
    add_character,
    list_characters_with_types,
    list_all_characters_with_optional_types,
)


def test_inner_join_returns_only_matching_types(connection):
    warrior_id = add_character_type(connection, "Warrior")
    mage_id = add_character_type(connection, "Mage")

    add_character(connection, "Ari", 100, 40, warrior_id)
    add_character(connection, "Mira", 60, 70, mage_id)
    add_character(connection, "Unknown", 50, 20, None)

    assert list_characters_with_types(connection) == [
        ("Ari", 40, "Warrior"),
        ("Mira", 70, "Mage"),
    ]


def test_left_join_keeps_character_without_type(connection):
    mage_id = add_character_type(connection, "Mage")

    add_character(connection, "Mira", 60, 70, mage_id)
    add_character(connection, "Unknown", 50, 20, None)

    assert list_all_characters_with_optional_types(connection) == [
        ("Mira", "Mage"),
        ("Unknown", None),
    ]
