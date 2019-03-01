import numpy as np
v0 = np.array([1,3,4])
v1 = np.full((3,3),0.1)
v2 = np.zeros((2,3))
v3 = np.ones((3,1))
v = v1*v3
v[0][0]=223
print(v)