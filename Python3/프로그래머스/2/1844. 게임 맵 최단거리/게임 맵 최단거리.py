from collections import deque

def bfs(maps, x, y):
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    n, m = len(maps), len(maps[0])
    
    visited = [[0 for i in range(m)] for j in range(n)]
    visited[x][y] = 1
    
    q = deque()
    q.append((x, y))
    
    while q:
        cx, cy = q.popleft()
        for dx, dy in dir:
            nx, ny = cx + dx, cy + dy
            if -1 < nx < n and -1 < ny < m and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx, ny))
    return visited

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = bfs(maps, 0, 0)
    
    if visited[n - 1][m - 1] == 0:
        return -1
    else:
        return visited[n - 1][m - 1]