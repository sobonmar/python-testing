"""Example tests to demonstrate hooks"""

import time


def test_fast_test():
    """Fast test"""
    assert 1 + 1 == 2


def test_slow_test():
    """Slow test"""
    time.sleep(1.2)
    assert True


def test_another_slow_operation():
    """Another slow test"""
    time.sleep(0.8)
    assert 2 * 2 == 4
