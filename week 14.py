# 1920번: 수찾기(이분탐색)
n = int(input())
a = sorted([int(i) for i in input().split()])
m = int(input())
num_list = [int(j) for j in input().split()]

def binary_search(target):
    left, right = 0, n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if a[mid] == target:
            return 1
        elif a[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return 0

def num_search():
    for num in num_list:
        print(binary_search(num))

num_search()

# 2805번: 나무자르기 (이분탐색)
def find_cutting_height(tree, m):
    left, right = 1, max(tree)

    while left <= right:
        mid = (left + right) // 2

        total_cut = 0
        for height in tree:
            if height >= mid:
                total_cut += height - mid

        if total_cut >= m:
            left = mid + 1
        else:
            right = mid - 1

    return right

n, m = map(int, input().split())
tree = list(map(int, input().split()))
result = find_cutting_height(tree, m)
print(result)

# 2110번: 공유기 설치