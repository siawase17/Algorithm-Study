# 12847번: 꿀아르바이트 (슬라이딩윈도우)
n, m = map(int, input().split())
pay = list(map(int, input().split()))

def maximum_profit(n, m, pay):
    max_profit = sum(pay[:m])
    current_profit = max_profit

    for i in range(m, n):
        current_profit = current_profit - pay[i - m] + pay[i]
        max_profit = max(max_profit, current_profit)

    return max_profit

result = maximum_profit(n, m, pay)
print(result)


# 2230번: 수고르기 (투포인터)
n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]

def get_minimum(n, m, nums):
    nums.sort()
    left, right = 0, 1
    min_diff = float('inf')

    while right < n:
        diff = nums[right] - nums[left]
        if diff >= m:
            min_diff = min(min_diff, diff)
            left += 1
            if left == right:
                right +=1
        else:
            right += 1

    return min_diff

result = get_minimum(n, m, nums)
print(result)

# 3078번: 좋은친구 (큐)
from collections import deque

n, k = map(int, input().split())
std_idx = [0] * 21
std_queue = deque([])
cnt = 0

for _ in range(n):
    name = input().rstrip()
    
    cnt += std_idx[len(name)]
    std_idx[len(name)] += 1

    if len(std_queue) == k:
        std_idx[std_queue.popleft()] -= 1
    std_idx.append(len(name))

print(cnt)
