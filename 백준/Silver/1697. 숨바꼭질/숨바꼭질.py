from collections import deque

def bfs(n, k):
    MAX = 100000
    visited = [0] * (MAX + 1)  # 방문 여부 + 시간 기록
    queue = deque([n])
    
    while queue:
        x = queue.popleft()
        
        if x == k:  # 동생 위치에 도달하면 시간 반환
            return visited[x]
        
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                queue.append(nx)

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(bfs(n, k))
