# create set with user input
set_A = set(input().split())
list = []

for _ in range(int(input())):
    set_N = set(input().split())
    
    # check is set A is superset set N
    list.append(set_A.issuperset(set_N))
    
print('False' if False in list else 'True')
    
# example : input   =   1 2 3 4 5
#                   = 1 
#                   = 4 5 6
#           outout = False
#            input   =   1 2 3 4 5
#                   = 1 
#                   = 3 4 5
#           outout = True
#   note : it is superset if all values from set n are in set a

