import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):  # 무방향 그래프
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node, visited):
    visited.add(node)
    for nxt in graph[node]:
        if nxt not in visited:
            dfs(nxt, visited)

visited = set()
count = 0
for i in range(1, n+1):
    if i not in visited:
        dfs(i, visited)
        count += 1

print(count)
