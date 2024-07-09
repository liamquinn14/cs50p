import pytest
from bank import value

def test_hello():
    assert value("hellooo") == 0
    assert value("hellooooo") == 0

def test_h():
    assert value("hamper") == 20
    assert value("hodeodo") == 20
    assert value("hlpplplp") == 20

def test_others():
    assert value("ol") == 100
    assert value("odfdfl") == 100
    assert value("ofdfgfl") == 100
    assert value("oasoadnl") == 100
    assert value("ello") == 100
    assert value("modsnd") == 100

def test_uppercase():
    assert value("HELLOO") == 0