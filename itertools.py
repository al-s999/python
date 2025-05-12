from itertools import combinations

n = int(input().strip())
A = tuple(input().strip().split(" "))
K = int(input().strip())

B = list(combinations(A,K))
print(len(list(filter( lambda x : "a" in x , B )))/len(B))