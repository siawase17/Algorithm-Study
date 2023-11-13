# 14719번: 빗물
def trap(h, w, height):
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height)-1
    left_max, right_max = height[left], height[right]
    
    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    
    return volume

h, w = map(int, input().split())
height = list(map(int, input().split()))
print(trap(h, w, height))

# 13414번: 수강신청
import sys
input = sys.stdin.readline

k, l = map(int, input().split())
s = dict()

for i in range(1, l+1):
    num = input().rstrip()
    s[num] = i
    
s = dict(sorted(s.items(), key = lambda x:x[1]))

cnt = 0
for i in s.keys():
    cnt += 1
    print(i)
    if cnt == k:
        break

# 2566번: 최댓값
arr = [list(map(int, input().split())) for _ in range(9)]
x = 0
y = 0
max_num = -1

for i in range(9):
    for j in range(9):
        if arr[i][j] > max_num:
            max_num = arr[i][j]
            x = i
            y = j
            
print(max_num)
print(x+1, y+1)

# 백준 numpy 사용불가
import numpy as np

arr = [list(map(int, input().split())) for _ in range(9)]
arr = np.array(arr)
max_arr = []

for i in arr:
    print(i)
    max_arr.append(max(i))

max_num = max(max_arr)
idx = np.where(arr == max_num)

print(max_num)
print(idx[0][0]+1, idx[1][0]+1)