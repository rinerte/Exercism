def score(x, y):
    shot = (x*x+y*y)**0.5
    if shot<=1.0:
        return 10
    elif shot<=5.0:
        return 5
    elif shot<=10.0:
        return 1
    return 0