import math

opposite = int(input())
adjacent = int(input())

print(round(math.degrees(math.atan(opposite/adjacent))), chr(176), sep="")