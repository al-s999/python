import string
import re
 
def score_words(arr):
    match = 0
    pattern = r"[aiueoy]"
    for item in arr:
        search = re.findall(pattern, str(item))
        if len(search) % 2 == 0:
            match += 2
        if len(search) % 2 == 1:
            match += 1 
    return match

n = int(input())
String = input().split()
String_lower = [i.lower() for i in String]
result = score_words(String_lower)
print(result)