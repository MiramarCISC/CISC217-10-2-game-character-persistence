def test_schema_creates_required_tables(connection):
    rows = connection.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        ORDER BY name
        """
    ).fetchall()

    names = [row[0] for row in rows]

    assert "character_types" in names
    assert "characters" in names
