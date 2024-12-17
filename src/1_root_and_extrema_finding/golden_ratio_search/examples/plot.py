import matplotlib.pyplot as plt
import numpy as np

def f(x):
    """Example function: f(x) = x^2"""
    return x**2

def golden_ratio_search_visualize(func, a, b, tol=1e-6, max_iterations=100):
    """
    Visualizes the initial and final steps of the Golden Ratio Search method for function minimization on a single plot.
    
    Parameters:
        func (function): The function to minimize.
        a (float): Initial lower bound of the interval.
        b (float): Initial upper bound of the interval.
        tol (float): Tolerance for stopping condition.
        max_iterations (int): Maximum number of iterations allowed.
    """
    # Golden ratio constant
    phi = (1 + np.sqrt(5)) / 2  # ~1.618
    inv_phi = 1 / phi  # ~0.618

    # Store initial a and b for plotting
    a_initial, b_initial = a, b

    # Compute initial internal points
    x1 = b - (b - a) * inv_phi
    x2 = a + (b - a) * inv_phi
    f1, f2 = func(x1), func(x2)

    iteration = 0
    intervals = [(a, b, x1, x2)]  # Store for visualization

    while (b - a > tol) and (iteration < max_iterations):
        if f1 > f2:  # Minimum is in [x1, b]
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (b - a) * inv_phi
            f2 = func(x2)
        else:  # Minimum is in [a, x2]
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - (b - a) * inv_phi
            f1 = func(x1)
        intervals.append((a, b, x1, x2))
        iteration += 1

    # Final a and b
    a_final, b_final = a, b

    # Generate x values for plotting
    x = np.linspace(a_initial - 1, b_initial + 1, 400)
    y = func(x)

    # Plot initial and final intervals on the same plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='$f(x) = x^2$', color='blue')
    plt.axhline(0, color='black', linewidth=0.5)

    # Initial step
    plt.scatter([a_initial, b_initial], [func(a_initial), func(b_initial)], color='red', label='Initial Brackets [a, b]')
    plt.scatter([intervals[0][2], intervals[0][3]], [func(intervals[0][2]), func(intervals[0][3])], color='green', label='Initial Points x1, x2')

    # Final step
    plt.scatter([a_final, b_final], [func(a_final), func(b_final)], color='purple', label='Final Brackets [a, b]')
    plt.scatter([x1, x2], [func(x1), func(x2)], color='orange', label='Final Points x1, x2')

    plt.title('Golden Ratio Search: Initial and Final Steps')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Initial conditions for Golden Ratio Search
a = -2
b = 2
golden_ratio_search_visualize(f, a, b)
