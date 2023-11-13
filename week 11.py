# 9934번: 완전이진트리
k = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(k)] # 각 레벨마다 담을 리스트 초기화

def binaryTree(level, left, right):
    if left <= right:
        mid = (left + right) // 2
        tree[level].append(arr[mid])
        binaryTree(level + 1, left, mid - 1)
        binaryTree(level + 1, mid + 1, right)

binaryTree(0, 0, len(arr) - 1)

for level_list in tree:
    print(*level_list)