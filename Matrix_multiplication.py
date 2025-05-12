import numpy as np

n = int(input())

matrix_a = []

matrix_b = []

for i in range(n):
    matrix_a.append(list(map(int, input().split())))
    

for i in range(n):
    matrix_b.append(list(map(int, input().split())))


print(np.dot(matrix_a,matrix_b))