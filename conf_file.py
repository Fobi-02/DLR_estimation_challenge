'''
File with data
'''

import numpy as np

# assumption of time difference between consecutive measurements
Dt = 0.1

# number of states [x,y,z,vx,vy,vz]
nx = 6


#  ____  _____                    _ _   _                                             #
# |___ \|  __ \                  (_) | (_)                                            
#   __) | |  | |  _ __   ___  ___ _| |_ _  ___  _ __    ___  ___ _ __  ___  ___  _ __ 
#  |__ <| |  | | | '_ \ / _ \/ __| | __| |/ _ \| '_ \  / __|/ _ \ '_ \/ __|/ _ \| '__|
#  ___) | |__| | | |_) | (_) \__ \ | |_| | (_) | | | | \__ \  __/ | | \__ \ (_) | |   
# |____/|_____/  | .__/ \___/|___/_|\__|_|\___/|_| |_| |___/\___|_| |_|___/\___/|_|   
#                | |                                                                  
#                |_|                                                                  

# Measurement model
H1 = np.array([
    [1,0,0,0,0,0],
    [0,1,0,0,0,0],
    [0,0,1,0,0,0]
])

# Measurement noise
R1 = np.array([
    [0.02,0,0],
    [0,0.02,0],
    [0,0,0.02]
])

# System model
A1 = np.array([
    [1,0,0,Dt,0,0],
    [0,1,0,0,Dt,0],
    [0,0,1,0,0,Dt],
    [0,0,0,1,0,0],
    [0,0,0,0,1,0],
    [0,0,0,0,0,1]
])

# System noise
sigma_a_2 = 5 # test value
Q1 = sigma_a_2 * np.array([
    [Dt**4/4, 0, 0, Dt**3/3, 0, 0],
    [0, Dt**4/4, 0, 0, Dt**3/3, 0],
    [0, 0, Dt**4/4, 0, 0, Dt**3/3],
    [Dt**3/3, 0, 0, Dt**2, 0, 0],
    [0, Dt**3/3, 0, 0, Dt**2, 0],
    [0, 0, Dt**3/3, 0, 0, Dt**2],
]) # from literature


#   _____                                                               
#  / ____|                                                              
# | |     __ _ _ __ ___   ___ _ __ __ _   ___  ___ _ __  ___  ___  _ __ 
# | |    / _` | '_ ` _ \ / _ \ '__/ _` | / __|/ _ \ '_ \/ __|/ _ \| '__|
# | |___| (_| | | | | | |  __/ | | (_| | \__ \  __/ | | \__ \ (_) | |   
#  \_____\__,_|_| |_| |_|\___|_|  \__,_| |___/\___|_| |_|___/\___/|_|   
                                                                       

# Measurement model
f = 500 #px
W = 640 #px
H = 480 #px
def h2(X):
    x = X[0]
    y = X[1]
    z = X[2] 
    return np.array([f/z*x+W/2, f/z*y+H/2])
# linearized measurement model
def H2(X):
    x = X[0]
    y = X[1]
    z = X[2]
    return np.array([
        [f/z, 0, -f*x/z**2, 0, 0, 0],
        [0, f/z, -f*y/z**2, 0, 0, 0]
    ])

# Measurement noise
R2 = np.array([
    [5,0],
    [0,5]
])

# System model
A2 = np.array([
    [1,0,0,Dt,0,0],
    [0,1,0,0,Dt,0],
    [0,0,1,0,0,Dt],
    [0,0,0,1,0,0],
    [0,0,0,0,1,0],
    [0,0,0,0,0,1]
])

# System noise
sigma_a_2 = 5 # test value
Q2 = sigma_a_2 * np.array([
    [Dt**4/4, 0, 0, Dt**3/3, 0, 0],
    [0, Dt**4/4, 0, 0, Dt**3/3, 0],
    [0, 0, Dt**4/4, 0, 0, Dt**3/3],
    [Dt**3/3, 0, 0, Dt**2, 0, 0],
    [0, Dt**3/3, 0, 0, Dt**2, 0],
    [0, 0, Dt**3/3, 0, 0, Dt**2],
]) # from literature