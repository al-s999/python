import numpy as np
a = list(map(int, input().split()))
r = [list(map(int, ''.join(list(input().split()[:a[1]])))) for i in range(a[0])]
result = np.max(np.min(np.array(r), axis=1))
print(result)