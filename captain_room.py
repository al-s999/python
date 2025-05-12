roomNumbers = input().split()
unq = set(roomNumbers)

for a in unq:
    roomNumbers.remove(a)
    
    if(a not in roomNumbers):
        print(int(a))
        break