import numpy as np

def arrays(arr):
    # reverse index in array, convert to numpy and set data type to float32
    r = np.array(arr[::-1], dtype=np.float32) 
    return r

arr = input().strip().split()
result = arrays(arr)
print(result)

#eaxmple : input = 1 2 3 4
#           output : [4. 3. 2. 1.]