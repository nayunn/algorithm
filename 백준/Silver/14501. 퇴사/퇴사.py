n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    t, p = arr[i]
    if i + t <= n:
        dp[i] = max(p + dp[i+t], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])