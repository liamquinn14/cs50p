import pytest
from twittr import shorten

def test_lowercase():
    assert shorten("jsfdjo") == "jsfdj"
    assert shorten("aeioufd") == "fd"
    assert shorten("aaaaaaaaaaaiiiiiiiiooooooouuuuuuun") == "n"
    assert shorten("aaaaaaaaaaaiiiiiiiiooooooouuuuuioioioiaoaoaoaoaoaoauun") == "n"
    assert shorten("Twitter") == "Twttr"
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("12345") == "12345"
    assert shorten("BCDFG") == "BCDFG"

def test_uppercase():
    assert shorten("AOAOOOOOOOOON") == "N"
    assert shorten("NNNNaaaaAAAAAAooooOooooOoOooOoiiiiiiiiJ") == "NNNNJ"
