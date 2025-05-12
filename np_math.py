import numpy as np

n, m = map(int, input().split())
a = [np.array(list(map(int, input().split()[:m]))) for _ in range(n)]
b = [np.array(list(map(int, input().split()[:m]))) for _ in range(n)]
print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.divide(a, b).astype(int))
print(np.mod(a, b))
print(np.power(a, b))