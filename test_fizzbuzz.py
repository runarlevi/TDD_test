import tests

def test_returns_number():
    assert tests.fizzbuzz(2) == 2

def test_returns_fizz_when_divisible_by_three():
    assert tests.fizzbuzz(3) == "Fizz"