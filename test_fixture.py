import pytest

# run before test
@pytest.fixture
def numbers():
    a = 10
    b = 20
    c = 25

    return [a, b, c]

#we know this is failing now we can give markers

@pytest.mark.xfail
def test_method1(numbers):
    x = 15
    assert numbers[0] == x

@pytest.mark.skip
def test_method2(numbers):
    y = 20
    assert numbers[1] == y

def test_method3(numbers):
    z = 25
    assert numbers[2] == z



#to run use pytest test_fixtures.py