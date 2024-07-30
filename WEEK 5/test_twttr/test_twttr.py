from twttr import shorten

def test_assert():
    assert shorten("Hello") == "Hll"
    assert shorten('David J Malan') == "Dvd J Mln"
    assert shorten("HELLO") == "HLL"
    assert shorten("H3LL0") == "H3LL0"
    assert shorten("H@LL#") == "H@LL#"
    assert shorten("Hello, World") == "Hll, Wrld"
