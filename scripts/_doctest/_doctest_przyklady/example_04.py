# Pułapki
"""
>>> None  # doctest: +SKIP
None
>>> None
"""

def greet(name):
    """
    znaki identyczne jak w interpreterze
    >>> greet("Ann")  # doctest: +SKIP
    "Witaj Ann!"
    >>> greet("Ann")  # doctest: +SKIP
    'Witaj Ann!'
    """
    return f"Witaj {name}!"


def long_text():
    """
    Długie linijki można łamać za pomocą znaku "\"
    >>> long_text()
    'Very long text aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
    """
    return "Very long text " + 52 * "a" + 52 * "b"



# Pułapki doctests
def mistakes():
    """
    Uwaga na precyzję float:

    # Trailing white spaces są czyszczone przez doctest podczas uruchamiania
    """

# Losowość:
# Kontrola nad losowością - wybieramy ziarno (seed) i wtedy zawsze mamy ten sam  "losowy" przebieg

import random


def generate_sample_data(size=5):
    """
    Generuje przykładowe dane do testowania algorytmów
    >>> random.seed(42)
    >>> generate_sample_data()
    [10, 1, 0, 4, 3]
    """
    return [random.randint(0, 10) for _ in range(size)]


def set_order_problem():
    """
    Problem z kolejnością w setach (w dictach od python 3.7 tego problemu już nie ma):

    Lepsze podejście:
    >>> set_order_problem()  # doctest: +SKIP
    {3, 1, 2}
    >>> s = set_order_problem()

    >>> 1 in s
    True
    >>> len(s)
    3
    >>> sorted(s)
    [1, 2, 3]
    """
    return {3, 1, 2}


def object_id_problem():
    """
    Problem z object id i memory addresses:

    >>> object()  # doctest: +ELLIPSIS
    <object object at 0x...>

    """
    return object()
