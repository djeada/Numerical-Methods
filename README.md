# Numerical Methods
This repository offers a comprehensive collection of numerical methods implemented in Python. It includes solutions to various mathematical problems, detailed explanations of each method, illustrative examples, and comparisons with prominent scientific libraries like Numpy, Scikit-Learn, and SciPy.

![Demo](https://user-images.githubusercontent.com/37275728/189313603-b409b2be-41b5-4de6-9d4f-2bd8f6e41565.png)

## Requirements

* Python 3.10+
* Whatever library is mentioned in the project's requirements.txt file.

## Installation

To run *.py* scripts the recommended approach is to use virtualenv:

    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ python path/to/main.py

For *.ipynb* notebooks you do not need to install anything locally on your PC. You may run all of the examples on the official website of Jupyter Notebooks using a demo version:

https://jupyter.org/try

To run the notebooks locally, use the following command:

    $ jupyter notebook path/to/notebook.ipynb

## Topics

### Root And Extrema Finding

Method | Notes | Implementation | Examples
------ | ----- | -------------- | --------
| Bisection Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/1_root_and_extrema_finding/bisection_method.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/bisection_search/implementation/bisection_search.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/bisection_search/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Secant Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/1_root_and_extrema_finding/secant_method.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/secant_method/implementation/secant_method.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/secant_method/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Relaxation Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/1_root_and_extrema_finding/relaxation_method.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/relaxation_method/implementation/relaxation_method.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/relaxation_method/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Golden Ratio Search | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/1_root_and_extrema_finding/golden_ratio_search.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/golden_ratio_search/implementation/golden_ratio_search.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/golden_ratio_search/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Newton Raphson | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/1_root_and_extrema_finding/newtons_method.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/newton_raphson/implementation/newton_raphson.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/newton_raphson/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Gradient Descent | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/1_root_and_extrema_finding/gradient_descent.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/gradient_descent/implementation/gradient_descent.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/gradient_descent/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |

### Systems Of Equations

Method | Notes | Implementation | Examples
------ | ----- | -------------- | --------
| Inverse Matrix | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/2_systems_of_equations/inverse_matrix.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/2_systems_of_equations/matrix_inverse/implementation/inverse_matrix.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/2_systems_of_equations/matrix_inverse/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Gaussian Elimination | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/2_systems_of_equations/gaussian_elimination.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/2_systems_of_equations/gaussian_elimination/implementation/gaussian_elimination.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/2_systems_of_equations/gaussian_elimination/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| LU Decomposition | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/2_systems_of_equations/lu_decomposition.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/2_systems_of_equations/lu_decomposition/implementation/lu_decomposition.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/2_systems_of_equations/lu_decomposition/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Gauss Seidel Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/2_systems_of_equations/gauss_seidel.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/2_systems_of_equations/gauss_seidel/implementation/gauss_seidel.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/2_systems_of_equations/gauss_seidel/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Jacobi Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/2_systems_of_equations/jacobi_method.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/2_systems_of_equations/jacobi_method/implementation/jacobi_method.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/2_systems_of_equations/jacobi_method/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |

### Differentiation

Method | Notes | Implementation | Examples
------ | ----- | -------------- | --------
| Taylor series | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/3_differentiation/taylor_series.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/3_derivatives/taylor_series/implementation/taylor_series.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/3_derivatives/taylor_series/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Forward difference | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/3_differentiation/forward_difference.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/3_derivatives/forward_difference/implementation/forward_difference.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/3_derivatives/forward_difference/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Backward difference | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/3_differentiation/backward_difference.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/3_derivatives/backward_difference/implementation/backward_difference.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/3_derivatives/backward_difference/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Central difference | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/3_differentiation/central_difference.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/3_derivatives/central_difference/implementation/central_difference.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/3_derivatives/central_difference/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |

### Integration

Method | Notes | Implementation | Examples
------ | ----- | -------------- | --------
| Midpoint Rule | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/4_integration/midpoint_rule.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/4_integration/midpoint_rule/implementation/midpoint_rule.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/tree/master/src/4_integration/midpoint_rule/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Trapezoidal Rule | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/4_integration/trapezoidal_rule.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/4_integration/trapezoid_rule/implementation/trapezoid_rule.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/tree/master/src/4_integration/trapezoid_rule/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Simpson's Rule | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/4_integration/simpsons_rule.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/4_integration/simpson/implementation/simpson_rule.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/tree/master/src/4_integration/simpson/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Monte Carlo Integration | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/4_integration/monte_carlo.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/4_integration/monte_carlo_integral/implementation/monte_carlo_integral.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/tree/master/src/4_integration/monte_carlo_integral/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |

### Matrices

Method | Notes | Implementation | Examples
------ | ----- | -------------- | --------
| Eigenvalues and Eigenvectors | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/5_matrices/eigenvalues_and_eigenvectors.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/5_matrices/eigenvalues_and_eigenvectors/implementation/eigenvalues_and_eigenvectors.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/tree/master/src/5_matrices/eigenvalues_and_eigenvectors/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Power Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/5_matrices/power_method.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/5_matrices/power_method/implementation/power_method.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/tree/master/src/5_matrices/power_method/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| QR Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/5_matrices/qr_method.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/5_matrices/qr_method/implementation/qr_method.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/tree/master/src/5_matrices/qr_method/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Eigenvalue Decomposition (EVD) | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/5_matrices/eigen_value_decomposition.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/5_matrices/eigen_value_decomposition/implementation/eigen_value_decomposition.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/tree/master/src/5_matrices/eigen_value_decomposition/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Singular Value Decomposition (SVD) | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/5_matrices/singular_value_decomposition.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/5_matrices/singular_value_decomposition/implementation/singular_value_decomposition.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/tree/master/src/5_matrices/singular_value_decomposition/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |

### Regression

Method | Notes | Implementation | Examples
------ | ----- | -------------- | --------
| Linear Interpolation | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/6_regression/linear_interpolation.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/6_regression/linear_interpolation/implementation/linear_interpolation.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Least Squares | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/6_regression/least_squares.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/6_regression/least_squares/implementation/least_squares.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Cubic Spline | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/6_regression/cubic_spline_interpolation.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/6_regression/cubic_spline/implementation/cubic_spline.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Lagrange Polynomial | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/6_regression/lagrange_polynomial_interpolation.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/6_regression/lagrange_polynomial/implementation/lagrange_polynomial.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/6_regression/lagrange_polynomial/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Newton's Polynomial | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/6_regression/newton_polynomial.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/6_regression/newton_polynomial/implementation/newton_polynomial.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/6_regression/newton_polynomial/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Gaussian Interpolation | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/6_regression/gaussian_interpolation.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/6_regression/gaussian_interpolation/implementation/gaussian_interpolation.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/6_regression/gaussian_interpolation/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Thin Plate Spline Interpolation | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/6_regression/thin_plate_spline_interpolation.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/6_regression/thin_plate_spline_interpolation/implementation/thin_plate_spline_interpolation.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/6_regression/thin_plate_spline_interpolation/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |

### Ordinary Differential Equations

Method | Notes | Implementation | Examples
------ | ----- | -------------- | --------
| Euler's Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/7_ordinary_differential_equations/eulers_method.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/7_ordinary_differential_equations/eulers/implementation/eulers.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/tree/master/src/7_ordinary_differential_equations/eulers/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Heun's Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/7_ordinary_differential_equations/heuns_method.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/7_ordinary_differential_equations/heuns/implementation/heuns.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/tree/master/src/7_ordinary_differential_equations/heuns/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Runge Kutta | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/7_ordinary_differential_equations/runge_kutta.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/7_ordinary_differential_equations/runge_kutta/implementation/runge_kutta.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/tree/master/src/7_ordinary_differential_equations/runge_kutta/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Picard's Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/7_ordinary_differential_equations/picards_method.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/7_ordinary_differential_equations/picard/implementation/picard.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/tree/master/src/7_ordinary_differential_equations/picard/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |

## References

### Books

- **Burden, Richard L.; Faires, J. Douglas**  
  *Numerical Analysis, 9th Edition*  
  [Amazon Link](https://amzn.to/4jcJ6Ku)

- **Epperson, James F.**  
  *An Introduction to Numerical Methods and Analysis*  
  [Amazon Link](https://amzn.to/4hZUdWl)

- **Press, William H.; Teukolsky, Saul A.; Vetterling, William T.; Flannery, Brian P.**  
  *Numerical Recipes: The Art of Scientific Computing, 3rd Edition*  
  [Amazon Link](https://amzn.to/4liZQ4w)

- **Heath, Michael T.**  
  *Scientific Computing: An Introductory Survey*  
  [Amazon Link](https://amzn.to/41YDYE5)

- **Giordano, Nicholas J.; Nakanishi, Hisao**  
  *Computational Physics*  
  [Amazon Link](https://amzn.to/4cmFQtN)

- **Chapra, Steven C.**  
  *Applied Numerical Methods with MATLAB for Engineers and Scientists*  
  [Amazon Link](https://amzn.to/42h0Z49)

- **LeVeque, Randall J.**  
  *Finite Difference Methods for Ordinary and Partial Differential Equations*  
  [Amazon Link](https://amzn.to/3RyCpqm)

### Online Resources

- [MIT OpenCourseWare: Linear Algebra](https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/)
- [Wikiversity: Cubic Spline Interpolation](https://en.wikiversity.org/wiki/Cubic_Spline_Interpolation)
- [Statnotes: Statistical Concepts by Dr. Garson](https://faculty.chass.ncsu.edu/garson/PA765/statnote.htm)
- [Numerical Methods Lectures, SDSU](https://jmahaffy.sdsu.edu/courses/s18/math541/Lectures.html)
- [Numerical Analysis: U of A Engineering Courses](https://engcourses-uofa.ca/books/numericalanalysis)
- [Numerical Methods by John Foster, UT Austin](https://johnfoster.pge.utexas.edu/numerical-methods-book)
- [Numerical Methods Course Material, NYU](https://math.nyu.edu/~stadler/num1/material/)
- [Fundamentals of Numerical Computation by Tobin A. Driscoll and Richard J. Braun](https://fncbook.com/)

## Contributing

Contributions are welcome! If you'd like to propose a major change, please open an issue first to discuss your ideas. 

When contributing, ensure you update relevant tests as needed to maintain the integrity of the project.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=djeada/Numerical-Methods&type=Date)](https://star-history.com/#djeada/Numerical-Methods&Date)
