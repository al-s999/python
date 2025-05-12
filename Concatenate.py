import numpy as np

n, m, p = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n+m)]

result = np.array(arr).flatten()
reshaped_result = result.reshape(-1, p)  
print(reshaped_result)
