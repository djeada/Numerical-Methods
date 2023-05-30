# Numerical Methods
Welcome to this collection of numerical methods implemented in Python from scratch! In this repository, you will find a variety of techniques for solving mathematical problems, along with the theoretical basis behind each method, examples of how to use the functions, and benchmarking against popular Python scientific libraries such as Numpy, Sickit-Learn, and SciPy. Whether you are a student looking to learn more about numerical methods or a researcher seeking efficient algorithms for your work, this repository has something for you. Explore the various directories to discover the methods and tools available, and feel free to use and adapt the code for your own purposes.

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
| Root Bracketing | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/1_root_and_extrema_finding/root_bracketing.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/root_bracketing/implementation/root_bracketing.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Picard Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/1_root_and_extrema_finding/picard_method.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/picard_method/implementation/picard_method.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Newton Raphson | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/1_root_and_extrema_finding/newton_raphson.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/newton_raphson/implementation/newton_raphson.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Bisection Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/1_root_and_extrema_finding/bisection_method.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/bisection_method/implementation/bisection_method.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Secant Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/1_root_and_extrema_finding/secant_method.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/secant_method/implementation/secant_method.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Golden Ratio Search | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/1_root_and_extrema_finding/golden_ratio_search.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/golden_ratio_search/implementation/golden_ratio_search.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Relaxation Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/1_root_and_extrema_finding/relaxation_method.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/relaxation_method/implementation/relaxation_method.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Gradient Descent | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/1_root_and_extrema_finding/gradient_descent.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/1_root_and_extrema_finding/gradient_descent/implementation/gradient_descent.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |

### Systems Of Equations

Method | Notes | Implementation | Examples
------ | ----- | -------------- | --------
| Gaussian Elimination | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/2_systems_of_equations/gaussian_elimination.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/2_systems_of_equations/gaussian_elimination/implementation/gaussian_elimination.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Gauss Seidel Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/2_systems_of_equations/gauss_seidel.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/2_systems_of_equations/gaussian_elimination/implementation/gaussian_elimination.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Inverse Matrix | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/2_systems_of_equations/inverse_matrix.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/2_systems_of_equations/gaussian_elimination/implementation/gaussian_elimination.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Jacobi Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/2_systems_of_equations/jacobi_method.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/2_systems_of_equations/gaussian_elimination/implementation/gaussian_elimination.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |

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
| Trapezoidal Rule | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/4_integration/trapezoidal_rule.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/4_integration/trapezoid_method/implementation/trapezoid_method.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/tree/master/src/4_integration/trapezoid_method/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Simpson's Rule | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/4_integration/simpsons_rule.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/4_integration/simpson/implementation/simpson.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/tree/master/src/4_integration/simpson/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Monte Carlo Integration | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/4_integration/monte_carlo.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/4_integration/simpson/implementation/simpson.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/tree/master/src/4_integration/simpson/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |

### Matrices

Method | Notes | Implementation | Examples
------ | ----- | -------------- | --------
| Power Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/5_matrices/power_method.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/5_matrices/power_method/implementation/power_method.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| QR Method | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/5_matrices/qr_method.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/5_matrices/inverse_power_method/implementation/inverse_power_method.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| LU Decomposition | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/5_matrices/lu_decomposition.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/5_matrices/qr_method/implementation/qr_method.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Eigenvalue Decomposition (EVD) | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/5_matrices/eigen_value_decomposition.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/5_matrices/qr_method/implementation/qr_method.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Singular Value Decomposition (SVD) | <a href="https://github.com/djeada/Numerical-Methods/blob/master/notes/5_matrices/singular_value_decomposition.md"><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/5_matrices/qr_method/implementation/qr_method.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |

### Regression

Method | Notes | Implementation | Examples
------ | ----- | -------------- | --------
| Linear Interpolation | <a href=""><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/6_regression/linear_interpolation/implementation/linear_interpolation.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Multiple Linear Regression | <a href=""><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/6_regression/multiple_linear_regression/implementation/multiple_linear_regression.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Least Squares | <a href=""><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/6_regression/least_squares/implementation/least_squares.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Cubic Spline | <a href=""><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/6_regression/cubic_spline/implementation/cubic_spline.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Lagrange Polynomial | <a href=""><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/6_regression/lagrange_polynomial/implementation/lagrange_polynomial.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/6_regression/lagrange_polynomial/examples/example.ipynb"><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |

### Ordinary Differential Equations

Method | Notes | Implementation | Examples
------ | ----- | -------------- | --------
| Euler's Method | <a href=""><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/7_ordinary_differential_equations/euler/implementation/euler.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |
| Runge Kutta | <a href=""><img src="https://img.icons8.com/color/344/markdown.png" height="50" /> </a> | <a href="https://github.com/djeada/Numerical-Methods/blob/master/src/7_ordinary_differential_equations/runge_kutta/implementation/runge_kutta.py"><img src="https://img.icons8.com/color/344/python.png" height="50" /> </a> | <a href=""><img src="https://img.icons8.com/fluency/344/jupyter.png" height="50" /> </a> |

## Refrences

* https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/
* https://en.wikiversity.org/wiki/Cubic_Spline_Interpolation
* https://faculty.chass.ncsu.edu/garson/PA765/statnote.htm
* https://jmahaffy.sdsu.edu/courses/s18/math541/Lectures.html
* https://engcourses-uofa.ca/books/numericalanalysis
* https://johnfoster.pge.utexas.edu/numerical-methods-book
* https://math.nyu.edu/~stadler/num1/material/

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
