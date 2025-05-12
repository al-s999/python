import re
codes = ""
for _ in range(int(input())):
    codes += input() + "\n"
codes = re.sub(r"(?<=\s)&&(?=\s)", " and ", codes)
codes = re.sub(r"(?<=\s)\|\|(?=\s)", " or ", codes)
print(codes)