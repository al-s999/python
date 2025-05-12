from collections import Counter
arr = []
number = 0
for _ in range(int(input())):
    text = input()
    arr.append(text)
result = Counter(arr)
print(len(result))
print(' '.join(map(str, result.values())))

    