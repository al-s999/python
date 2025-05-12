import re
s = input()
small = re.findall("[a-z]",s)
big = re.findall("[A-Z]",s)
num = re.findall("[0-9]",s)
oddnum = [int(n) for n in num if int(n) %2 != 0]
evennum = [int(n) for n in num if int(n) %2 == 0]    
print(*(sorted(small) + sorted(big) + sorted(oddnum) + sorted(evennum)), sep='')