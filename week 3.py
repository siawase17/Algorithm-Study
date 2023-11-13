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