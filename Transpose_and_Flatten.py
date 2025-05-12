import numpy as np

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = np.array(arr)
t = np.transpose(result)
f = result.flatten()

print(t)
print(f)