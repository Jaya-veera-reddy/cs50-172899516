from um import count

def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1

def test_um_with_punctuation():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um... uh... um!") == 2

def test_um_as_substring():
    assert count("yummy") == 0
    assert count("aluminum") == 0
    assert count("sum") == 0

def test_multiple_ums():
    assert count("Um, thanks, um...") == 2
    assert count("Um, um, um") == 3

def test_edge_cases():
    assert count("um") == 1
    assert count("Hello, um, world") == 1
    assert count("This is, um... CS50.") == 1
    assert count("Um... what are regular expressions?") == 1
    assert count("Um, thanks, um, regular expressions make sense now.") == 2
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2

if __name__ == "__main__":
    import pytest
    pytest.main()
