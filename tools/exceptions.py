# pylint: disable=missing-module-docstring
class TooManyCalls(Exception):
    """
    Exception raised when the maximum number of function calls is exceeded.

    Args:
        message (str, optional): Custom error message. Defaults to "Too many calls".
    """
    def __init__(self, message: str = "Too many calls") -> None:
        super().__init__(message)
