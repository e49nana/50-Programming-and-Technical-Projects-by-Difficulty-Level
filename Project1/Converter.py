def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def pascal_to_bar(pa):
    return pa / 100000

def bar_to_pascal(bar):
    return bar * 100000

def joule_to_kwh(j):
    return j / 3.6e6

def kwh_to_joule(kwh):
    return kwh * 3.6e6
