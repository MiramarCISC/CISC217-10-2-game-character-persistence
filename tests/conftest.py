import sqlite3
import pytest

from cisc217_week10 import create_schema


@pytest.fixture
def connection():
    connection = sqlite3.connect(":memory:")
    create_schema(connection)
    yield connection
    connection.close()
