from bank import value

def test_price():
    assert value("hello") == 0
    assert value("Hey") == 20
    assert value("by") == 100