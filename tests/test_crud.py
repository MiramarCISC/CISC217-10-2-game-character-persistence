from cisc217_week10 import (
    add_character_type,
    add_character,
    get_character,
    list_characters,
    update_health,
    delete_character,
)


def test_add_and_get_character(connection):
    mage_id = add_character_type(connection, "Mage")
    character_id = add_character(connection, "Mira", 60, 70, mage_id)

    assert get_character(connection, character_id) == (
        character_id,
        "Mira",
        60,
        70,
        mage_id,
    )


def test_get_character_returns_none_when_missing(connection):
    assert get_character(connection, 9999) is None


def test_list_characters_orders_by_id(connection):
    warrior_id = add_character_type(connection, "Warrior")

    first_id = add_character(connection, "Ari", 100, 40, warrior_id)
    second_id = add_character(connection, "Theo", 80, 30, warrior_id)

    rows = list_characters(connection)

    assert [row[0] for row in rows] == [first_id, second_id]


def test_update_health(connection):
    warrior_id = add_character_type(connection, "Warrior")
    character_id = add_character(connection, "Ari", 100, 40, warrior_id)

    changed = update_health(connection, character_id, 75)

    assert changed == 1
    assert get_character(connection, character_id)[2] == 75


def test_delete_character(connection):
    healer_id = add_character_type(connection, "Healer")
    character_id = add_character(connection, "Theo", 80, 30, healer_id)

    changed = delete_character(connection, character_id)

    assert changed == 1
    assert get_character(connection, character_id) is None
