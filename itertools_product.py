from itertools import product

A = []
n = input().split()
m = input().split()

A.append(n)
A.append(m)

result = list(product(*A))
formatted_result = ' '.join(f'({x}, {y})' for x, y in result)
print(formatted_result)