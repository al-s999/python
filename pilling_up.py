from collections import deque

num_test = int(input())

for _ in range(num_test):
    
    num_block = int(input())
    blocks = deque(map(int, input().split()))
    pile = []
    
    while blocks:
        
        if blocks[0] <= blocks[-1]:
            pile.append(blocks.pop())
        
        else:
            pile.append(blocks.popleft())
            
    if pile == sorted(pile, reverse=True):
        print('Yes')
    
    else:
        print('No')