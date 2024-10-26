from bank import value

def test_value():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("Hey") == 20
    assert value("greetings") == 100
    assert value("What's up") == 100
    assert value("Good morning") == 100

if __name__ == "__main__":
    test_value()
    print("All tests passed.")
