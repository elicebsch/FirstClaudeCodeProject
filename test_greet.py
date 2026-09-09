from greet import greet


def test_greet_with_name():
    assert greet("Elia") == "Hello, Elia!"


def test_greet_without_name():
    assert greet("") == "Hello, there!"
