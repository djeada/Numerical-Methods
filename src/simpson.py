def simpson(f, a, b, n=100):
    h = (b - a) / n
    x = [0] * (n + 1)
    x[0] = a
    result = 0

    for i in range(n):
        x[i + 1] = a + h * k

    for k in range(1, n // 2 + 1):
        result += f(x[2 * k - 2]) + 4 * f(x[2 * k - 1]) + f(x[2 * k])

    return h * result / 3
