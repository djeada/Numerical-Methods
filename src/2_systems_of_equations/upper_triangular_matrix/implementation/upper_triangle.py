def solve_equation_system(A, b):
    def upper_triangle(A, b):
        """
        Works only for square matrices.
        """

        n = numpy.size(b)

        for k in range(n - 1):
            for i in range(k + 1, n):
                s = A[i, k] / A[k, k]  # scaling factor
                for j in range(k, n):
                    A[i, j] = A[i, j] - s * A[k, j]
                b[i] = b[i] - s * b[k]

    upper_triangle(A, b)

    n = numpy.size(b)
    x = numpy.zeros(n)

    for k in range(n - 1, -1, -1):
        s = 0.0
        for j in range(k + 1, n):
            s = s + A[k, j] * x[j]
        x[k] = (b[k] - s) / A[k, k]

    return x

