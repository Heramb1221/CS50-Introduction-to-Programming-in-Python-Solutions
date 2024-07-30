from fuel import convert, gauge
import pytest

def test_input():
    assert convert('3/4') == 75
    assert convert('1/4') == 25
    assert convert('4/4') == 100
    assert convert('0/4') == 0

def errors():
    with pytest.raises(ZeroDivisionError):
        convert('2/0')
    with pytest.raises(ValueError):
        convert('3/2')

def test_output():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(50) == '50%'
