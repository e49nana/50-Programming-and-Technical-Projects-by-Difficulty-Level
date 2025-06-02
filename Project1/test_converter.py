from converter import *

def test_all():
    assert celsius_to_fahrenheit(0) == 32
    assert round(fahrenheit_to_celsius(212), 2) == 100.0
    assert celsius_to_kelvin(0) == 273.15
    assert kelvin_to_celsius(273.15) == 0
    assert pascal_to_bar(100000) == 1
    assert bar_to_pascal(1) == 100000
    assert joule_to_kwh(3600000) == 1
    assert kwh_to_joule(1) == 3600000
    print("All tests passed.")

if __name__ == "__main__":
    test_all()
