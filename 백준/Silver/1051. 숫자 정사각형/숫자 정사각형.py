n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
#print(arr[0][1]) # 0행 1열
square = [1]

for i in range (n):
    for j in range (m):
        now = arr[i][j]
        for z in range (j+1,m):
            if now == arr[i][z]:
                length = z - j
                if length < n-i and length < m-j :
                    if now == arr[i+length][j]==arr[i+length][z]:
                        square.append(length)

square.sort()
if len(square) == 1:
    print(1)
else:
    print((square[-1]+1)**2)