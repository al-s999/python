import numpy as np
a = list(map(int, input().split()))
if a[0] == a[1]:
    r = [list(map(int, ''.join(list(input().split())))) for i in range(a[0])]
    result = np.prod(np.sum(np.array(r), axis=0))
    print(result)
else :
    print("Error")