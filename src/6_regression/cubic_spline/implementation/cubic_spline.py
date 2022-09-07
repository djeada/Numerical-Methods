import bisect


def cubic_spline(x_data, y_data):

    if x_data.size != y_data.size:
        raise Exception("X and Y vectors must have equal number of elements.")

    if x_data.size < 3:
        raise Exception("X and Y vectors have to contain at least 3 elements.")

    n = x_data.size

    def create_tri_diag_matrix_data(n, h):
        A = [h[i] / (h[i] + h[i + 1]) for i in range(n - 2)]
        A += [0]
        B = [2] * n
        C = [0]
        C += [h[i + 1] / (h[i] + h[i + 1]) for i in range(n - 2)]
        return A, B, C

    def compute_D(n, h, y_data):
        result = [0]
        result += [
            6
            * (
                (y_data[i + 1] - y_data[i]) / h[i]
                - (y_data[i] - y_data[i - 1]) / h[i - 1]
            )
            / (h[i] + h[i - 1])
            for i in range(1, n - 1)
        ]
        result += [0]
        return result

    def solve_tri_diag_sy_datastem(A, B, C, D):
        c_p = C + [0]
        d_p = [0] * len(B)
        x_data = [0] * len(B)

        c_p[0] = C[0] / B[0]
        d_p[0] = D[0] / B[0]

        for i in range(1, len(B)):
            c_p[i] = c_p[i] / (B[i] - c_p[i - 1] * A[i - 1])
            d_p[i] = (D[i] - d_p[i - 1] * A[i - 1]) / (B[i] - c_p[i - 1] * A[i - 1])

        x_data[-1] = d_p[-1]

        for i in range(len(B) - 2, -1, -1):
            x_data[i] = d_p[i] - c_p[i] * x_data[i + 1]

        return x_data

    def result_function(point):
        idx_data = min(bisect.bisect(x_data, point) - 1, n - 2)
        z = (point - x_data[idx_data]) / h[idx_data]
        C = coeffs[idx_data]
        return (((C[0] * z) + C[1]) * z + C[2]) * z + C[3]

    h = [x_data[i + 1] - x_data[i] for i in range(len(x_data) - 1)]
    A, B, C = create_tri_diag_matrix_data(n, h)
    D = compute_D(n, h, y_data)
    M = solve_tri_diag_sy_datastem(A, B, C, D)

    coeffs = [
        [
            (M[i + 1] - M[i]) * h[i] * h[i] / 6,
            M[i] * h[i] * h[i] / 2,
            (y_data[i + 1] - y_data[i] - (M[i + 1] + 2 * M[i]) * h[i] * h[i] / 6),
            y_data[i],
        ]
        for i in range(n - 1)
    ]

    return result_function
