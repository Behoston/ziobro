import pytest

from ziobro.exit import ziobro


def test_exit_success():
    with pytest.raises(SystemExit) as e:
        ziobro()
    assert e.value.code == 0
