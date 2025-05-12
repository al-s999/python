n, m = list(map(int, input().split()))
a = [letter for letter in (input() for _ in range(n))]

print("\n".join(
    " ".join(str(i + 1) for i in range(n) if a[i] == letter) or "-1"
    for letter in (input() for _ in range(m))
))