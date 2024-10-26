import pytest
from plates import is_valid
def main():
    test_1()
    test_2()
    test_3()
    test_4()

def test_2():
    assert is_valid("eagt")==True
    assert is_valid("fexdwez6")==False
    assert is_valid("f")==False

def test_4():
    assert is_valid("dfvt")==True
    assert is_valid("faf,sd")==False

def test_1():
    assert is_valid("23")==False
    assert is_valid("cs")==True

def test_3():
    assert is_valid("cs05")==False
    assert is_valid("cs50")==True
    assert is_valid("cs50d")==False

if __name__ == "__main__":
    pytest.main()
