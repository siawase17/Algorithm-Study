# 프로그래머스: 게임맵 최단거리
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    queue = deque([(0, 0, 1)])  
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x, y, distance = queue.popleft()
        
        if x == m - 1 and y == n - 1:
            return distance
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (nx < 0 or nx >= m) or (ny < 0 or ny >= n) or maps[ny][nx] == 0:
                continue
            
            if not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny, distance + 1))
    
    return -1
