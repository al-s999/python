from collections import deque
d = deque()
for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == "pop":
        d.pop()
    elif cmd[0] == "popleft":
        d.popleft()
    elif cmd[0] == "clear":
        d.clear()
    elif cmd[0] in ("remove", "append","appendleft","extend","extendleft","count","reverse","rotate",):
        eval(f"d.{cmd[0]}({cmd[1]})")
print(' '.join(map(str,d)))

