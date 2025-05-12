import numpy as np
a = list(map(int, input().split()))
r = [list(map(int, ''.join(list(input().split()[:a[1]])))) for i in range(a[0])]
arr = np.array(r)
print(np.mean(arr, axis=1), np.var(arr, axis=0), round(np.std(arr), 11), sep='\n')