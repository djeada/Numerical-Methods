import numpy as np


def qr_method(a, num_iter=10):
    """
    returns all eigenvalues
    """

    def qr_decomposition(a):
        def householder_transformation(a):
            v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
            v[0] = 1

            return v, 2 / np.dot(v.T, v)

        m, n = a.shape
        r = a.copy()
        q = np.identity(m)

        for i in range(n):
            v, tau = householder_transformation(r[i:, i, np.newaxis])

            H = np.identity(m)
            H[i:, i:] -= tau * np.dot(v, v.T)
            r = np.dot(H, r)
            q = np.dot(H, q)

        q = q[:n].T
        r = np.triu(r[:n])
        return q, r

    for i in range(num_iter):
        q, r = qr_decomposition(a)
        a = np.dot(r, q)

    return np.diagonal(a)
