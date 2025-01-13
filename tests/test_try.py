import pytest

from tests import _TEST_ROOT


@pytest.mark.parametrize("a,b", [(1, 1), (1, 2), (1, 1)])
@pytest.mark.parametrize("c", [2, 3, 4])
def test_param_me(a, b, c):
    # hello world
    # ok
    assert a == b


class TestDad:
    def test_boy(self):
        print("hello" + _TEST_ROOT)
        a = 2
        b = 3
        c = 2
        d = [1, 2, 3, 4]
        assert 1 == 1
