from NUMB3RS import validate

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True

    assert validate("cat") == False
    assert validate("256.0.0.1") == False
    assert validate("1.256.0.1") == False
    assert validate("1.1.256.0") == False
    assert validate("1.1.0.1000") == False