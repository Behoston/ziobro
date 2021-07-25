import pytest

from ziobro.object import Ziobro
from ziobro.object import ziobro


def test_ziobro_is_singleton():
    assert Ziobro(70000000) is ziobro


def test_ziobro_act_like_a_zero_int():
    assert ziobro == 0
    assert ziobro * ziobro == 0
    assert ziobro * 2 == 0
    assert 2 * ziobro == 0
    assert ziobro + ziobro == 0
    assert ziobro + 2 == 2
    assert 2 + ziobro == 2
    assert ziobro / 2 == 0
    with pytest.raises(ZeroDivisionError):
        ziobro / ziobro
    with pytest.raises(ZeroDivisionError):
        2 / ziobro
    assert ziobro ** ziobro == 1


def test_ziobro_object_is_callable():
    assert ziobro('wykop.pl') == 0


def test_ziobro_can_exit_successfully():
    with pytest.raises(SystemExit) as e:
        ziobro.exit()
    assert e.value.code == 0
