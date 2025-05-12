from itertools import groupby
groups = []
uniquekeys = []
data = input().strip()
for k, g in groupby(data): 
    groups.append(len(list(g)))      
    uniquekeys.append(int(k))
print(*list(zip(groups,uniquekeys)))