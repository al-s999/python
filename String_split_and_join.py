def split_and_join(line):
    # write your code here
    l = line.split(" ")
    li = "-".join(l)
    return li
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)