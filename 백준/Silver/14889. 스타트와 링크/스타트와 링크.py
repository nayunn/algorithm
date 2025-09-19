import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input().strip())
S = [list(map(int, input().split())) for _ in range(N)]

# W[i][j] = S[i][j] + S[j][i] (i<j만 사용)
W = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        W[i][j] = S[i][j] + S[j][i]

players = list(range(N))
min_diff = float('inf')

# 0번을 A팀에 고정 → 같은 분할 중복 제거
others = players[1:]
half = N // 2

for comb in combinations(others, half - 1):
    teamA = {0, *comb}
    teamB = set(players) - teamA

    # 점수 계산 (i<j만 순회)
    A_score = 0
    B_score = 0
    for i in range(N):
        for j in range(i+1, N):
            if i in teamA and j in teamA:
                A_score += W[i][j]
            elif i in teamB and j in teamB:
                B_score += W[i][j]

    min_diff = min(min_diff, abs(A_score - B_score))

print(min_diff)
