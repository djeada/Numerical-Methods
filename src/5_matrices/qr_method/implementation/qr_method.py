import numpy as np
from scipy.linalg import hessenberg


def qr_decomposition(A: np.ndarray):
    return np.linalg.qr(A)


def qr_algorithm(A: np.ndarray, tol: float = 1e-8, max_iterations: int = 2000):
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square.")

    A_k = hessenberg(A).astype(float)
    eigenvalues = []

    iterations = 0  # Track the number of iterations
    while A_k.shape[0] > 0:
        for _ in range(max_iterations):
            iterations += 1
            if A_k.shape[0] == 1:
                eigenvalues.append(A_k[0, 0])
                A_k = np.empty((0, 0))
                break

            if abs(A_k[-1, -2]) < tol:
                eigenvalues.append(A_k[-1, -1])
                A_k = A_k[:-1, :-1]
                break

            if A_k.shape[0] == 2:
                trace = np.trace(A_k)
                det = np.linalg.det(A_k)
                discriminant = (trace / 2) ** 2 - det

                if discriminant >= 0:
                    eigenvalues.append(trace / 2 + np.sqrt(discriminant))
                    eigenvalues.append(trace / 2 - np.sqrt(discriminant))
                else:
                    eigenvalues.append(trace / 2 + 1j * np.sqrt(-discriminant))
                    eigenvalues.append(trace / 2 - 1j * np.sqrt(-discriminant))
                A_k = np.empty((0, 0))
                break

            Q, R = qr_decomposition(A_k)
            A_k = R @ Q

        if iterations >= max_iterations:
            raise ValueError(
                "QR algorithm did not converge within the maximum number of iterations."
            )

    return np.sort(eigenvalues)


def qr_algorithm_with_shifts(
    A: np.ndarray, tol: float = 1e-8, max_iterations: int = 2000
):
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square.")

    A_k = hessenberg(A).astype(float)
    eigenvalues = []

    iterations = 0  # Track the number of iterations
    while A_k.shape[0] > 0:
        for _ in range(max_iterations):
            iterations += 1
            if A_k.shape[0] == 1:
                eigenvalues.append(A_k[0, 0])
                A_k = np.empty((0, 0))
                break

            if abs(A_k[-1, -2]) < tol:
                eigenvalues.append(A_k[-1, -1])
                A_k = A_k[:-1, :-1]
                break

            if A_k.shape[0] == 2:
                trace = np.trace(A_k)
                det = np.linalg.det(A_k)
                discriminant = (trace / 2) ** 2 - det

                if discriminant >= 0:
                    eigenvalues.append(trace / 2 + np.sqrt(discriminant))
                    eigenvalues.append(trace / 2 - np.sqrt(discriminant))
                else:
                    eigenvalues.append(trace / 2 + 1j * np.sqrt(-discriminant))
                    eigenvalues.append(trace / 2 - 1j * np.sqrt(-discriminant))
                A_k = np.empty((0, 0))
                break

            submatrix = A_k[-2:, -2:]
            trace = np.trace(submatrix)
            det = np.linalg.det(submatrix)
            discriminant = (trace / 2) ** 2 - det

            if discriminant >= 0:
                shift = trace / 2 + np.sign(trace / 2) * np.sqrt(discriminant)
            else:
                shift = trace / 2

            Q, R = qr_decomposition(A_k - shift * np.eye(A_k.shape[0]))
            A_k = R @ Q + shift * np.eye(A_k.shape[0])

        if iterations >= max_iterations:
            raise ValueError(
                "QR algorithm with shifts did not converge within the maximum number of iterations."
            )

    return np.sort(eigenvalues)
