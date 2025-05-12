import numpy as np
matrix = []
l = int(input())
matrix = [list(map(float, input().split()[:l])) for _ in range(l)]
det = np.linalg.det(matrix)
output = f"{det:.2f}"
if output.endswith(".00"):
    output = output[:-1]
print(output)