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

