from cisc217_week10 import (
    add_character_type,
    add_character,
    strong_characters,
)


def test_strong_characters_filters_and_sorts(connection):
    warrior_id = add_character_type(connection, "Warrior")
    mage_id = add_character_type(connection, "Mage")
    healer_id = add_character_type(connection, "Healer")

    add_character(connection, "Ari", 100, 40, warrior_id)
    add_character(connection, "Mira", 60, 70, mage_id)
    add_character(connection, "Theo", 80, 30, healer_id)
    add_character(connection, "Nova", 50, 90, mage_id)

    rows = strong_characters(connection, 50)

    assert [row[1] for row in rows] == ["Nova", "Mira"]
