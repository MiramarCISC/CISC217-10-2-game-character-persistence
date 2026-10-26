from cisc217_week10 import (
    add_character_type,
    add_character,
    get_character,
)


def test_sql_like_text_is_stored_as_data(connection):
    type_id = add_character_type(
        connection,
        "Mage'); DROP TABLE characters; --",
    )

    character_id = add_character(
        connection,
        "Ari'); DROP TABLE character_types; --",
        100,
        40,
        type_id,
    )

    row = get_character(connection, character_id)

    assert row[1] == "Ari'); DROP TABLE character_types; --"

    table = connection.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
          AND name = 'character_types'
        """
    ).fetchone()

    assert table == ("character_types",)
