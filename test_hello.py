import pytest
from hellov2 import hello


def test_hello():
    hello("David") == "hello, David"


def test_mytest():
    with pytest.raises(TypeError):
        test_hello()


test_mytest()


# 6: 51
