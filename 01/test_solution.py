import pytest
from solution import strict


def test_no_arguments():
    @strict
    def func():
        return True

    result = func()
    assert result is True


def test_no_error_1(func_four_diff_params):
    result = func_four_diff_params(5, 5.5, "string", True)
    assert result == (5, 5.5, "string", True)


def test_no_error_2(func_four_diff_params):
    result = func_four_diff_params(
        -12345,
        99999999.999,
        "supersupersupersupersuperlonglonglonglonglongstringstringstringstring",
        False,
    )
    assert result == (
        -12345,
        99999999.999,
        "supersupersupersupersuperlonglonglonglonglongstringstringstringstring",
        False,
    )


def test_no_error_3(func_four_diff_params):
    result = func_four_diff_params(0, 0.0, "", False)
    assert result == (0, 0.0, "", False)


def test_no_error_4(func_four_diff_params):
    result = func_four_diff_params(0, 0.0, "", False)
    assert result == (0, 0.0, "", False)


def test_error_1(func_four_diff_params):
    with pytest.raises(TypeError):
        func_four_diff_params("Hello, world!", 0.0, "", False)


def test_error_2(func_four_diff_params):
    with pytest.raises(TypeError):
        func_four_diff_params(1024, 8, "", False)


def test_error_3(func_four_diff_params):
    with pytest.raises(TypeError):
        func_four_diff_params(1, 1024.1024, True, False)


def test_error_4(func_four_diff_params):
    with pytest.raises(TypeError):
        func_four_diff_params(1, 1024.1024, "String123", 5)
