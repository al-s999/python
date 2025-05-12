import itertools
n, m = map(int, input().split())
l=[]
for _ in range(n):
    l.append(set(list(map(int, input().split()))[1:]))

combinations = list(itertools.product(*l))  

big_num = 0
for i in range(len(combinations)):
    big_num = max(sum([x**2 for x in combinations[i]]) % m ,big_num)
print(big_num)