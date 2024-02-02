from poetry_suburi.main import read_item, root


def test_root():
    assert root() == {"message": "Hello World"}


def test_read_item():
    assert read_item(1) == {"item_id": 1}
