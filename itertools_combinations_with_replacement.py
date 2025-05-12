from itertools import combinations_with_replacement
s, k = input().split(" ")

# solving 1
result = combinations_with_replacement(sorted(s),int(k))
for i in result:
    print(''.join(i))

# solving 2
[print(''.join(x)) for x in (combinations_with_replacement(sorted(s),int(k)))]