from ziobro.version import to_ziobro
from ziobro.version import ziobro


def test_version_full():
    assert ziobro(2, 8, 1) == '000.000000000.00'


def test_version_without_patch():
    assert ziobro(2, 1) == '000.00.0'


def test_version_minimal():
    assert ziobro() == '0.0.0'


def test_to_ziobro_minimal():
    assert to_ziobro('2') == '000.0.0'


def test_to_ziobro_minor():
    assert to_ziobro('3.11') == '0000.000000000000.0'


def test_to_ziobro_full():
    assert to_ziobro('4.1.5') == '00000.00.000000'
