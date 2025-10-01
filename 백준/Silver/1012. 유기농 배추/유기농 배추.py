import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우 방향
directions = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]   # n행 m열
    visited = [[False]*m for _ in range(n)]

    # 배추 심기
    for _ in range(k):
        y, x = map(int, input().split())  # y=열, x=행
        graph[x][y] = 1
    
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1
    
    print(count)
