def square(number):
    """name here.

    description here"""
    if number>64 or number<1:
        raise ValueError("square must be between 1 and 64")    
    return 2 ** (number - 1)

def total():
    """name here.

    description here"""
    return (2 ** 64) - 1
