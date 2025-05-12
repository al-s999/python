import re
s = input()
match = re.search(r"([a-zA-Z0-9])\1+", s)
print(match.group(1) if match else -1)
    