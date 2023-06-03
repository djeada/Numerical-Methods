def midpoint_rule(a, b, f, n=10):
    step = (b - a)/n
    total = 0.0
    mid = a + step/2

    while (mid < b):
        total += step * f(mid)
        mid += step

    return total
