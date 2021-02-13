from sandwich_maker.prices import calculateTotalPrice
import pytest


def test_calculate_total_price_should_return_price_of_single_item():
    result = calculateTotalPrice(["wheat"])
    assert result == 1.0


def test_calculate_total_price_should_return_total_price_of_multiple_items():
    result = calculateTotalPrice(["wheat", "chicken"])
    assert result == 2.0


def test_calculate_total_price_should_not_add_unknown_items():
    result = calculateTotalPrice(["wheat", "alligator"])
    assert result == 1.0