import numpy as np

n = input().split()
result = np.array(n, dtype=int)
print(np.reshape(result,(3,3)))
