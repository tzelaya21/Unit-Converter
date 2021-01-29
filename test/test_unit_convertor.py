from code.Unit_convertor import Distance, Weight, Temperature
import pytest


@pytest.mark.parametrize('val1, _from1, _to1, _results1', [
    (10, "METERS", "FEET", 32.8084),
    (20, "FEET", "INCHES", 240),
    (7832312, "INCHES", "MILES", 123.6160354)
])
def test_Distance(val1, _from1, _to1, _results1):
    assert Distance(val1, _from1, _to1) == _results1


@pytest.mark.parametrize('val2, _from2, _to2, _results2', [
    (21, "KG", "GRAMS", 21000),
    (34, "KILOGRAMS", "OUNCES", 1199.31),
    (450, "OUNCES", "POUNDS", 28.125)
    (45000, "GRAMS", "OUNCES", 1587.3283),
    (34232, "OUNCES", "KILOGRAMS", 970.46088)
])
def test_Weight(val2, _from2, _to2, _results2):
    assert Weight(val2, _from2, _to2) == _results2


@pytest.mark.parametrize('val3, _from3, _to3, _results3', [
    (104, "FAHRENHEIT", "CELSIUS", 40),
    (89, "CELSIUS", "FAHRENHEIT", 192.2),
    (37, "CELSIUS", "FAHRENHEIT", 98.6)
])
def test_Temperature(val3, _from3, _to3, _results3):
    assert Temperature(val3, _from3, _to3) == _results3

