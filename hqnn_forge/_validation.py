import numbers
import numpy as np

def check_int(value, name: str, *, minimum: int, allow_none: bool = False) -> int | None:
    """Validate that a value is an integer (excluding booleans) and at least `minimum`.

    Parameters
    ----------
    value : Any
        The value to validate.
    name : str
        The parameter or variable name (used in error messages).
    minimum : int
        The inclusive lower bound for the integer value.
    allow_none : bool, default=False
        Whether None is an accepted value.

    Returns
    -------
    int or None
        The validated integer, or None if `allow_none` is True and `value` is None.
    """
    if allow_none and value is None:
        return None
        
    if isinstance(value, bool) or not isinstance(value, (numbers.Integral, np.integer)):
        raise TypeError(f"'{name}' must be an integer, got {type(value).__name__}")
    
    int_val = int(value)
    if int_val < minimum:
        raise ValueError(f"'{name}' must be at least {minimum}, got {int_val}")
        
    return int_val