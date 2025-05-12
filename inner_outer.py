import numpy as np
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(np.inner(np.array(a), np.array(b)))
print(np.outer(np.array(a), np.array(b)))