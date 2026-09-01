'''
File with functions for Extended Kalman filter algorithm
'''

import numpy as np

# prediction step of EKF
# in this case the system model is linear so the function is the same as in the KF
def prediction(x, A, P, Q):
    x = A @ x 
    P = A @ P @ A.T + Q
    return x, P

# update step of EKF
def update(x, z, h, H, P, R, nx):
    k = P @ H(x).T @ np.linalg.inv(H(x) @ P @ H(x).T + R)
    x = x + k @ (z - h(x))
    P = (np.eye(nx) - k @ H(x)) @ P
    return x, P