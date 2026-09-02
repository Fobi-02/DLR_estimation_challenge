import matplotlib.pyplot as plt
import numpy as np
import conf_file as conf
import EKF

# loading the data
ground_truth  = np.loadtxt("data/ground_truth_3d_position.csv", delimiter=",", skiprows=1)
camera_sensor = np.loadtxt("data/measurements_2d_camera.csv", delimiter=",", skiprows=1)

# Kalman filter
P = np.eye(conf.nx)
x = np.array([-1.8, -0.5, 7.9, 0, 0, 0])
x_EKF_B = np.zeros((np.size(camera_sensor[:,0]), conf.nx))
for i in range(np.size(camera_sensor[:,0])):
    # prediction step
    x, P = EKF.prediction(x, conf.A2, P, conf.Q2)
    # update step
    x, P = EKF.update(x, camera_sensor[i,:], conf.h2, conf.H2, P, conf.R2, conf.nx)
    # storing the result
    x_EKF_B[i, :] = x

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(ground_truth[:,0],ground_truth[:,1],ground_truth[:,2], s=1, color='red',label='ground truth')
ax.plot(x_EKF_B[:,0],x_EKF_B[:,1],x_EKF_B[:,2], color='blue',label='EKF')
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("z [m]")
ax.legend()
plt.show()