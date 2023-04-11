def add_integer(a, b=98):
    if type(a) not in [float, int] or type(b) not in [float, int]:
        raise TypeError("a and b must be either integers or floats.")
    return int(a) + int(b)
