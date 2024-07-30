from working import convert

def test_convert():
    assert convert('09:00 AM to 3:00 PM') == '09:00 to 15:00'
    assert convert('03:11 AM to 8:59 AM') == '03:11 to 08:59'