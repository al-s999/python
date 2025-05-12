import re

def count_substring(string, sub_string):
    result = len(re.findall(f'(?={sub_string})', string))
    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)