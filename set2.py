
m = int(input())
arr1 = set(map(int, input().split()))
n = int(input())
arr2 = set(map(int, input().split()))
result = sorted(arr1.symmetric_difference(arr2))
for i in result:
    print(i)