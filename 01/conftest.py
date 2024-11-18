import pytest
from solution import strict


@pytest.fixture
def func_four_diff_params():
    @strict
    def func(
        first_param: int,
        second_param: float,
        third_param: str,
        fourth_param: bool,
    ):
        return first_param, second_param, third_param, fourth_param

    return func
