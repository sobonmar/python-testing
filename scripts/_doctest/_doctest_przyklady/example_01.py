# Doctesty funkcji
import doctest

def sum_(a: float, b: float) -> float:
    """Add two numbers together.
    
    Args:
        a: First number to add
        b: Second number to add
        
    Returns:
        Sum of a and b

    Examples:
    >>> sum_(1, 2)
    3
    >>> sum_(0, 0)
    0

    >>> sum_(1.5, 2.8)
    4.3

    >>> sum_(0.2, 0.1)  # doctest: +SKIP
    0.3
    >>> round(sum_(0.2, 0.1), 1)
    0.3
    >>> abs(sum_(0.2, 0.1) - 0.3) < 0.00001
    True

    >>> a = 1
    >>> b = 2
    >>> sum_(a, b)
    3

    >>> res = 0
    >>> for t in [(1, 2), (3, 4)]:
    ...     res += sum_(t[0], t[1])
    ...
    >>> res
    10

    >>> for t in [(1, 2), (3, 4)]:
    ...     sum_(t[0], t[1])
    ...
    3
    7
    """
    return a + b


def div(a: float, b: float) -> float:
    """Divide two numbers.
    
    Args:
        a: Dividend (number to be divided)
        b: Divisor (number to divide by)
        
    Returns:
        Result of a divided by b
        
    Raises:
        ValueError: If b is zero

    Example:
    >>> div(4, 0)
    Traceback (most recent call last):
      ...
    ValueError: Cannot divide by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# Sposoby uruchamiania
# python -m doctest example_01.py
# python -m doctest example_01.py -v  (verbose)

if __name__ == "__main__":
    doctest.testmod()
    # python example_01.py -v
