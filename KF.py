'''
File with functions for Kalman filter algorithm
'''

import numpy as np

# prediction step of KF
def prediction(x, A, P, Q):
    x = A @ x
    P = A @ P @ A.T + Q
    return x, P

# update step of KF
def update(x, z, H, P, R, nx):
    k = P @ H.T @ np.linalg.inv(H @ P @ H.T + R)
    x = x + k @ (z - H @ x)
    P = (np.eye(nx) - k @ H) @ P
    return x, P
