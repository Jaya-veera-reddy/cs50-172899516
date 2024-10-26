from numb3rs import validate

def test_valid_ip_addresses():
    assert validate("127.0.0.1") == True
    assert validate("192.168.0.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("8.8.8.8") == True

def test_invalid_ip_addresses():
    assert validate("275.3.6.28") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("123.456.78.90") == False
    assert validate("cat") == False
    assert validate("192.168.0") == False
    assert validate("192.168.0.256") == False

def test_edge_cases():
    assert validate("") == False
    assert validate(" ") == False
    assert validate("...") == False
    assert validate("0.0.0.0.0") == False
    assert validate("256.256.256.256") == False
    assert validate("01.02.03.04") == True  # Leading zeros are valid

# To run the tests, use pytest in the terminal
# pytest test_numb3rs.py
