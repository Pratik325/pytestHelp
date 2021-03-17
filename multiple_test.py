import pytest
import warnings
warnings.filterwarnings('ignore')



# def test_method1():
#     x = 5
#     y = 10
#     assert x == y


# def test_method2():
#     a = 15
#     b = 20
#     assert a + 5 == b

# #run this using == > py.test -k method1 -v //method1 = function name



#creating markers
@pytest.mark.one
def test_method1():
    x = 5
    y = 10
    assert x == y

@pytest.mark.two
def test_method2():
    a = 15
    b = 20
    assert a + 5 == b


# run marker wala using py.test -m one/two

