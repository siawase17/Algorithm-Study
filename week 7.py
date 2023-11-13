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

# 24479번: 깊이우선탐색1
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

from collections import defaultdict

n, m, r = map(int, input().split())
cnt = 1
visited = [0] * (n+1)
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) 

def dfs(start):
    global cnt
    visited[start] = cnt
    graph[start].sort() 
    
    for i in graph[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)  

dfs(r)
for i in range(1, n+1):
    print(visited[i])
