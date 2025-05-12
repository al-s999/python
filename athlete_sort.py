if __name__ == '__main__':
    n,m = map(int, input().split())

    arr = []

    for _ in range(n):
        row = input().rstrip().split()
        # covert string to int if it is a digit
        row = [int(x) if x.lstrip('-').isdigit() else x for x in row]
        arr.append(row)
        
    # set index from shorting, note index start from first type integer
    k = int(input()) 
    
    # sort array by k and if have mix of string and integer output is error
    results = sorted(arr, key=lambda x: x[k])
    for result in results:
        result = [str(x) for x in result]
        print(' '.join(result))
        
# example input: = 3 2
#                  row  = orange 4
#                       = apple 2
#                       = banana 1
#                  k = 0
#          output       = banana 1
#                      = apple 2
#                      = orange 4