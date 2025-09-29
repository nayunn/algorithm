from collections import deque

n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n+1)} 

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(node, visited):
    visited.add(node)
    print(node, end=" ")
    for nxt in sorted(graph[node]): 
        if nxt not in visited:
            DFS(nxt, visited)

def BFS(start):
    visited = set()
    q = deque([start])

    while q:
        node = q.popleft()
        if node in visited:
            continue
        visited.add(node)
        print(node, end=" ")
        for nxt in sorted(graph[node]):
            if nxt not in visited:
                q.append(nxt)

DFS(v, set())
print()
BFS(v)
