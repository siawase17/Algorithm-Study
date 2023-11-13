# 프로그래머스: 배달 (다익스트라)
def solution(N, road, K):
    answer = 0

    dist_list = [float('inf')] * (N + 1)

    dist_list[1] = 0

    for i in range(1, N) : 
        for [a,b,c] in road :
            dist_list[b] = min(dist_list[b], dist_list[a] + c)
            dist_list[a] = min(dist_list[a], dist_list[b] + c)

    for i in dist_list : 
        if i <= K : 
            answer += 1

    return answer

# 프로그래머스: 해킹 (다익스트라)
import sys
input = sys.stdin.readline
import heapq

t = int(input())
inf = float('inf')

def dijkstra(N, D, C):
    g = [[] for _ in range(N + 1)]
    for _ in range(D):
        a, b, s = map(int, input().split())
        g[b].append((a, s))

    dist = [inf for _ in range(N + 1)]
    dist[C] = 0

    h = [(0, C)] 
    time = 0
    cnt = 0

    while h:
        cost, node = heapq.heappop(h)
        if dist[node] >= cost:
            for n, c in g[node]:
                newdist = dist[node] + c
                if newdist < dist[n]:
                    dist[n] = newdist
                    heapq.heappush(h, (newdist, n))
    
    reachable_distances = [dist[i] for i in range(1, N+1) if dist[i] != inf]
    cnt = len(reachable_distances)
    time = max(reachable_distances) if reachable_distances else 0
    
    return f"{cnt} {time}"

for _ in range(t):
    n, d, c = map(int, input().split())
    print(dijkstra(n, d, c))

# 프로그래머스: 모음사전 (DFS)
def dfs(word, words, vowels):
    words.append(word)
    
    if len(word) == 5:
        return

    for vowel in vowels:
        dfs(word + vowel, words, vowels)

def solution(word):
    vowels = 'AEIOU'
    words = []
    dfs('', words, vowels)
    
    return words.index(word)