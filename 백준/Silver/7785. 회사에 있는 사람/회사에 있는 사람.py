n = int(input())
s = set()

for _ in range(n):
    name, state = input().split()
    if state == "enter":
        s.add(name)
    else:
        s.discard(name)

for name in sorted(s, reverse=True):
    print(name)