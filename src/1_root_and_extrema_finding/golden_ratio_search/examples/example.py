def objective_function(x):
    return (x - 2) ** 2  # Minimum at x = 2

minimum = golden_ratio_search(objective_function, 0, 4)
print("Minimum:", minimum)
