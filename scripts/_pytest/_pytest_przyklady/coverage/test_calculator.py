"""Tests for calculator module - demonstrating partial coverage"""

from calculator import add, divide, is_positive, get_grade


def test_add_basic():
    """Test basic addition"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_divide_normal():
    """Test normal division"""
    assert divide(10, 2) == 5.0


def test_get_grade_a():
    """Test grade A"""
    assert get_grade(95) == "A"
    assert get_grade(90) == "A"


def test_get_grade_b():
    """Test grade B"""
    assert get_grade(85) == "B"
    assert get_grade(70) == "B"

# Missing tests that would bring coverage to >90%:
# 1. Test divide by zero error
# 2. Test is_positive with positive number  
# 3. Test is_positive with negative number
# 4. Test get_grade negative score error
# 5. Test get_grade F (score < 70)