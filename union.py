n = int(input())
s1 = set(map(int, input().split()[:n]))
m = int(input())
s2 = set(map(int, input().split()[:m]))
print(len(s1.union(s2)))

#alternative 2
print(len(set(map(int, input().split()[1:])).union(set(map(int, input().split()[1:])))))