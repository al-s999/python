import re
arr =[]
pattern = r"^[+-.]?[0-9]*\.[0-9]+$"
for _ in range(int(input())):
    s = input()
    arr.append(str(bool(re.match(pattern, s))))

for i in arr:
    print(i)