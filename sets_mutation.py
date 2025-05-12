n = int(input())
A = set(map(int, input().split()))
N = int(input())
for i in range(N):
    cmd, num = input().split()
    if(cmd == "iu"):
        A.intersection_update([*map(int, input().split())])
    elif(cmd == "u"):
        A.update([*map(int, input().split())])
    elif(cmd == "du"):
        A.difference_update([*map(int, input().split())])
    else:
        A.symmetric_difference_update([*map(int, input().split())])

print(sum(A))