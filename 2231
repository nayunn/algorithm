N = int(input())
length = len(str(N))   # 자릿수
start = max(1, N - length*9)

for i in range(start,N):
    result = i
    for j in str(i):
         result += int(j)
    if result == N:
        print(i)
        break
else: 
    print(0)