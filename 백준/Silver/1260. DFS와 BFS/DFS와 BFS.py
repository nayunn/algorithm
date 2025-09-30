import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 1. 입력 받기
n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 2. 인접 리스트 정렬 (작은 번호 우선 탐색 위해)
for i in range(1, n+1):
    graph[i].sort()

# 3. DFS 구현
visited_dfs = [False] * (n + 1)
dfs_order = []

def dfs(node):
    visited_dfs[node] = True
    dfs_order.append(node)
    for nxt in graph[node]:
        if not visited_dfs[nxt]:
            dfs(nxt)

# 4. BFS 구현
visited_bfs = [False] * (n + 1)
bfs_order = []

def bfs(start):
    q = deque()
    q.append(start)
    visited_bfs[start] = True
    while q:
        node = q.popleft()
        bfs_order.append(node)
        for nxt in graph[node]:
            if not visited_bfs[nxt]:
                visited_bfs[nxt] = True
                q.append(nxt)

# 5. 탐색 실행
dfs(v)
bfs(v)

# 6. 출력
print(*dfs_order)
print(*bfs_order)
