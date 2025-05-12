n = int(input())

#input ke tuple dan tidak lebih dari n
arr = tuple(map(int,input().split()[:n]))
#jika semua elemen tidak negatif dan ada bilangan palindrom dalam tuple
if all(x >= 0 for x in arr) and any(str(x) == str(x)[::-1] for x in arr):
    print(True)
else:
    print(False)

# example : input = n = 3
#                   arr = 12 21 44
#           output = true
#   because tuple not have negative number and have palindrome number (ex: 12, 21)