# test_twttr.py

from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("AEIOUaeiou") == ""
    assert shorten("CS50") == "CS50"
    assert shorten("123456") == "123456"
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("") == ""
