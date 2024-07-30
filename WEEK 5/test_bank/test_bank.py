from bank import value

def test_assert():

    assert value("hello") == 0

    assert value("HELLO") == 0

    assert value("hi") == 20

    assert value("goodbye") == 100

    assert value("hello world") == 0

    assert value("HELLO WORLD") == 0

