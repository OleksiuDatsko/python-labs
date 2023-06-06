"""
This module provides custom exception classes.

Exceptions:
    TooManyCalls: Exception raised when the maximum number of function calls is exceeded.
"""


class TooManyCalls(Exception):
    """
    Exception raised when the maximum number of function calls is exceeded.

    Args:
        message (str, optional): Custom error message. Defaults to "too many calls".
    """

    def __init__(self, message: str = "too many calls") -> None:
        super().__init__(message)


class NoPlantInTheGardenException(Exception):
    # pylint: disable=line-too-long
    """
    Exception raised when there are no plants in the garden.

    Args:
        message (str, optional): Custom error message. Defaults to "There is no plant in the garden."
    """

    def __init__(self, message: str = "There is no plant in the garden") -> None:
        super().__init__(message)


class NotEnoughPlantsException(Exception):
    # pylint: disable=line-too-long
    """
    Exception raised when there are not enough plants in the garden.

    Args:
        message (str, optional): Custom error message. Defaults to "There are not enough plants in the garden."
    """

    def __init__(
        self, message: str = "There are not enough plants in the garden"
    ) -> None:
        super().__init__(message)


class NoSuchModeException(Exception):
    """Exception raised when an invalid mode is encountered.

    Attributes:
        message (str): The error message associated with the exception.
    """

    def __init__(self, message: str = "There is no such mode") -> None:
        super().__init__(message)
