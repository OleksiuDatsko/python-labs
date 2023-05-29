# pylint: disable=line-too-long
"""
This module provides decorators for function and method behavior.

Decorators:
    limit_calls: A decorator that limits the number of calls to a function.
    number_of_arguments_in_method: A decorator that counts and prints the number of arguments in a method.
"""
from functools import wraps
from types import FunctionType

from tools.exceptions import TooManyCalls


def limit_calls(max_calls: int = 3):
    """
    A decorator that limits the number of calls to a function.

    Raises:
        TooManyCalls: If the maximum number of calls is exceeded.
    """

    def inner(func: FunctionType):
        calls = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            Wrapper function that tracks the number of calls and limits them.

            Args:
                *args: Positional arguments passed to the decorated function.
                **kwargs: Keyword arguments passed to the decorated function.

            Returns:
                The result of the decorated function.

            Raises:
                TooManyCalls: If the maximum number of calls is exceeded.
            """
            nonlocal calls
            if calls >= max_calls:
                raise TooManyCalls()
            calls += 1
            return func(*args, **kwargs)

        return wrapper

    return inner


def number_of_arguments_in_method(func):
    """
    A decorator that counts and print number of arguments in a method.
    """

    @wraps(func)
    def inner(*args, **kwargs):
        """
        Inner function that counts ad print number of arguments and calls the decorated method.

        Args:
            *args: Positional arguments passed to the decorated method.
            **kwargs: Keyword arguments passed to the decorated method.

        Returns:
            The result of the decorated method.
        """
        print(f"function {func.__name__} has {len(args)} arguments in method")
        return func(*args, **kwargs)

    return inner
