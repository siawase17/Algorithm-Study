# 5639번: 이진검색트리
numbers = []
while True:
    num = input()
    
    if not num:
        break
    
    numbers.append(int(num))
    
def postorder(arr):
    if not arr:
        return []
    
    root = arr[0]
    left = []
    right = []
    
    for i in arr[1:]:
        if i < root:
            left.append(i)
        else:
            right.append(i)
        
    left_postorder = postorder(left)
    right_postorder = postorder(right)
    
    return left_postorder + right_postorder + [root]

ans = postorder(numbers)
for i in ans:
	print(i)

# 11725번: 트리의 부모찾기
from collections import deque

n = int(input())
visited = [False] * (n+1)
answer = [0] * (n+1)
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[b].append(a)
    tree[a].append(b)


def bfs(tree, node, visited):
    que = deque([node])
    visited[node] = True
    while que:
        x = que.popleft()
        for i in tree[x]:
            if not visited[i]:
                answer[i] = x
                que.append(i)
                visited[i] = True

bfs(tree,1,visited)

for i in range(2, n+1):
        print(answer[i])