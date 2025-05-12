def solve(s):
    s_list = s.split(" ")
    
    # get value from input and use lambda for get fisrt character and upper the charecter
    result = list(map(lambda i: i.capitalize(), s_list))
    # give space in list result ([hello,world] -> Hello World)
    return " ".join(result)

if __name__ == '__main__':

    s = input()

    result = solve(s)
    
    print(result)

# example :  input = hello world
#            output =  Hello World