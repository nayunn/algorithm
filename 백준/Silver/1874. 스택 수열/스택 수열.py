n = int(input())
arr = [int(input()) for _ in range(n)]
stack=[]
result = []
idx=0

for i in range(1, n+1):
    stack.append(i)
    result.append("+")

    while stack and arr[idx]==stack[-1]:
        stack.pop()
        result.append("-")
        idx+=1


if idx == n:
    print("\n".join(result))
else:
    print("NO")