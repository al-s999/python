def print_formatted(number):
    # your code goes here
    for i in range(1, number+1):
        width = len(bin(number)[2:])
        # Option 1
        print(f"{i:{width}d} "
              f"{i:{width}o} "
              f"{i:{width}X} "
              f"{i:{width}b}")
              
        # Option 2    
        # print(f"{i}".rjust(width),
        #       "{0:o}".format(i).rjust(width),
        #       "{0:X}".format(i).rjust(width),
        #       "{0:b}".format(i).rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)