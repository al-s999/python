import re
patern = r"#[0-9a-fA-F]{3,6}[;,)]"
css = ""
for _ in range(int(input())):
    css += input() + "\n"
matches = re.findall(patern, css)
for value in matches:
    print(value[:-1])