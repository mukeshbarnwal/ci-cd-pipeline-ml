import pytest


# parameterize is used to pass the fixed parameters
@pytest.mark.parametrize("a,b,expected", [(1,2,3), (2,3,5), (3,4,7)])
def test_add_parametrize(a,b,expected):
    assert a+b == expected
    

# fixture is used to fix certrain variables so that you can use it for different test functions
@pytest.fixture
def a():
    return 2
# a is fixed to 2

@pytest.fixture
def b():
    return 3
# b is fixed to 3

def test_add(a, b):
    assert a + b == 5

def test_mul(a, b):
    assert a * b == 6
