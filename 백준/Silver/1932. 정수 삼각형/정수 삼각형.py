import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*len(arr[i]) for i in range(n)]
dp[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:  # 맨 왼쪽
            dp[i][j] = dp[i-1][j] + arr[i][j]
        elif j == i:  # 맨 오른쪽
            dp[i][j] = dp[i-1][j-1] + arr[i][j]
        else:  # 가운데
            dp[i][j] = arr[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))
