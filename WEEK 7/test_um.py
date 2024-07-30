from um import count

def test_input():
    assert count("yummy") == 0
    assert count("num") == 0

def test_nospace():
    assert count("um") == 1
    assert count("um, can i... um... help?") == 2

def test_case():
    assert count(" um ") == 1
    assert count(" UM ") == 1