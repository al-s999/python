s = set(map(int, input().split()[1:]))
for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == "pop" and s:
        s.pop()
    elif cmd[0] in ("remove", "discard"):
        eval(f"s.{cmd[0]}({cmd[1]})")
print(sum(s))