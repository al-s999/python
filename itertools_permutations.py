from itertools import permutations

s, k = input().split()

s = str(s)
k = int(k)
result = sorted(list(permutations(s,k)))

for i in result:
    print(''.join(i))