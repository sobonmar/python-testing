# PYTEST MARKERS - najpopularniejsze

import pytest


# WBUDOWANE MARKERY
@pytest.mark.skip("Always skip this test")
def test_skipped():
    assert False  # Never runs


@pytest.mark.skipif(True, reason="Skip if condition true")
def test_conditional_skip():
    assert False


@pytest.mark.xfail(reason="Expected to fail")
def test_expected_fail():
    assert False  # Passes because we expect failure


@pytest.mark.parametrize("input,expected", [(2, 4), (3, 9)])
def test_parametrized(input, expected):
    assert input ** 2 == expected


# WŁASNE MARKERY (zdefiniowane w pytest.ini)
@pytest.mark.slow
def test_slow_operation():
    """Slow test - run with: pytest -m slow"""
    import time
    time.sleep(0.1)
    assert True


@pytest.mark.integration
def test_integration():
    """Integration test - run with: pytest -m integration"""
    assert True


@pytest.mark.unit
def test_unit():
    """Unit test - run with: pytest -m unit"""
    assert True


@pytest.mark.smoke
def test_smoke():
    """Smoke test - run with: pytest -m smoke"""
    assert True


@pytest.mark.api
def test_api():
    """API test - run with: pytest -m api"""
    assert True


# KOMBINACJE MARKERÓW
@pytest.mark.slow
@pytest.mark.integration
def test_slow_integration():
    """Multiple markers"""
    assert True


# URUCHOMIENIE:
# pytest -m slow           # Tylko slow
# pytest -m "not slow"     # Wszystko oprócz slow
# pytest -m "slow or unit" # slow LUB unit
# pytest -m "slow and api" # slow I api
# pytest --markers         # Lista wszystkich markerów