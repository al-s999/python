import re
arr = []
Start = 0
s = input().strip()
k = input().strip()
while Start <= len(s):
    string = re.search(k,s[Start:])
    if(string):
        arr.append(tuple([string.start() + Start, string.end() -1 + Start]))
        Start +=  int(string.span()[0]) + 1
    else :
        break
if len(arr) == 0 :
    print((-1, -1))
else :
    [print(x) for x in arr] if len(arr)!= 0 else print(-1)