import pytest
import app


@pytest.fixture(scope="class")
def test_setup():
    pytest.actions = app.CRUD()

    yield
