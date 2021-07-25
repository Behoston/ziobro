from ziobro.func import ziobro


def test_func_return_0_with_no_arguments():
    assert ziobro() == 0


def test_func_return_0_with_args():
    assert ziobro('a') == 0
    assert ziobro('a', 1, None) == 0


def test_func_return_0_with_kwargs():
    assert ziobro(name='a') == 0
    assert ziobro(name='a', value=1, filter=None) == 0


def test_func_return_0_with_args_and_kwargs():
    assert ziobro('a', 'b', value=1, filter=None) == 0
