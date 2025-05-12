tests_num = int(input())
for _ in range(tests_num):
    
#   input value of set a and set b
    set_A = set(map(int, input().split()))
    set_B = set(map(int, input().split()))

#   print type booelan 
    print(set_A.issubset(set_B))
    
# example : input   = 2
#                   = 1 2 3
#                   = 1 2 3 4 5
#           output  = True
#           input   = 1 2 3 4
#                   = 1 2 3
#           output  = False
#   note = set a.issubset(set b) is return booelan value, if all value from set a are in set b return True else False