def func(x):
    return np.sin(x)


derivatives = [
    np.sin,
    np.cos,
    lambda x: -np.sin(x),
    lambda x: -np.cos(x),
]  # Up to the fourth derivative
point = 0
n = 5

taylor_expansion = taylor_series(func, derivatives, point, n)
print("Taylor series expansion:")
print(taylor_expansion)
