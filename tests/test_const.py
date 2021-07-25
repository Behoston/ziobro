def test_const_is_const():
    from ziobro.const import ZIOBRO

    assert ZIOBRO == 0

    from ziobro.const import ZIOBRO

    assert ZIOBRO == 0
