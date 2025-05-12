n = int(input())
s1 = set(map(int, input().split()[:n]))
m = int(input())
s2 = set(map(int, input().split()[:m]))
print(len(s1.difference(s2)))

#alternative 2
print(len(set(map(int, input().split()[1:])).difference(set(map(int, input().split()[1:])))))

n = int(input())
s1 = set(map(int, input().split()[:n]))
m = int(input())
s2 = set(map(int, input().split()[:m]))
print(len(s1.symmetric_difference(s2)))

#alternative 2
print(len(set(map(int, input().split()[1:])).symmetric_difference(set(map(int, input().split()[1:])))))