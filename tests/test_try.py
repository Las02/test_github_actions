import pytest

from tests import _TEST_ROOT


@pytest.mark.parametrize("a,b", [(1, 1), (1, 2), (1, 1)])
@pytest.mark.parametrize("c", [2, 3, 4])
def test_param_me(a, b, c):
    # hello world
    # ok
    # hello world
    assert a == a


class TestDad:
    def test_boy(self):
        print("hello" + _TEST_ROOT)








        assert 1 == 1
