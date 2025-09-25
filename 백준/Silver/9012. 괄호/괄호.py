n = int(input())
arr = [input().strip() for _ in range(n)]

def vps(vpss):
    s = list(vpss)
    i = 0
    while i < len(s):
        if i > 0 and s[i] == ')' and s[i-1] == '(':
            s.pop(i)
            s.pop(i-1)
            i -= 1
        else:
            i += 1
    return "YES" if not s else "NO"

for i in arr:
    print(vps(i))
