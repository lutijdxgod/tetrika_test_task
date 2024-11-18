from typing import Any, Callable
from inspect import signature


def strict(func: Callable[..., Any]):
    sig = signature(func)
    annotations: dict = func.__annotations__

    def wrapper(*args, **kwargs):
        bound_parametrs = sig.bind(*args, **kwargs)

        for argument_name, argument_value in bound_parametrs.arguments.items():
            if not isinstance(argument_value, annotations[argument_name]):
                raise TypeError

        function_result = func(*args, **kwargs)

        return function_result

    return wrapper
