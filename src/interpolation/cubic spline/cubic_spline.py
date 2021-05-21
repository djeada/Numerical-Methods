import bisect


def cubic_spline(x, y):
    n = len(x)

    if n != len(y):
        raise ValueError(
            "Provided lists have diffrent lengths: len(x)={}, len(y)={}".format(
                n, len(y)
            )
        )

    if n < 3:
        raise ValueError("You have to provide at least three points")

    def create_tri_diag_matrix(n, h):
        A = [h[i] / (h[i] + h[i + 1]) for i in range(n - 2)]
        A += [0]
        B = [2] * n
        C = [0]
        C += [h[i + 1] / (h[i] + h[i + 1]) for i in range(n - 2)]
        return A, B, C

    def compute_D(n, h, y):
        result = [0]
        result += [
            6
            * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])
            / (h[i] + h[i - 1])
            for i in range(1, n - 1)
        ]
        result += [0]
        return result

    def solve_tri_diag_system(A, B, C, D):
        c_p = C + [0]
        d_p = [0] * len(B)
        X = [0] * len(B)

        c_p[0] = C[0] / B[0]
        d_p[0] = D[0] / B[0]

        for i in range(1, len(B)):
            c_p[i] = c_p[i] / (B[i] - c_p[i - 1] * A[i - 1])
            d_p[i] = (D[i] - d_p[i - 1] * A[i - 1]) / (B[i] - c_p[i - 1] * A[i - 1])

        X[-1] = d_p[-1]

        for i in range(len(B) - 2, -1, -1):
            X[i] = d_p[i] - c_p[i] * X[i + 1]

        return X

    def result_function(val):
        idx = min(bisect.bisect(x, val) - 1, n - 2)
        z = (val - x[idx]) / h[idx]
        C = coeffs[idx]
        return (((C[0] * z) + C[1]) * z + C[2]) * z + C[3]

    h = [x[i + 1] - x[i] for i in range(len(x) - 1)]
    A, B, C = create_tri_diag_matrix(n, h)
    D = compute_D(n, h, y)
    M = solve_tri_diag_system(A, B, C, D)

    coeffs = [
        [
            (M[i + 1] - M[i]) * h[i] * h[i] / 6,
            M[i] * h[i] * h[i] / 2,
            (y[i + 1] - y[i] - (M[i + 1] + 2 * M[i]) * h[i] * h[i] / 6),
            y[i],
        ]
        for i in range(n - 1)
    ]

    return result_function
