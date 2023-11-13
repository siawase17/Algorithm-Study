# 프로그래머스: 더맵게 (최소힙, 그리디)
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) #최소힙 

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        mixed = first + (second * 2)
        heapq.heappush(scoville, mixed)

        answer += 1

    return answer

# 14426번: 접두사 찾기 (이진탐색)
def binary_search(n_list, prefix):
    left, right = 0, len(n_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if n_list[mid].startswith(prefix):
            return True
        elif n_list[mid] < prefix: # 알파벳 순서
            left = mid + 1 # 검색 범위가 오른쪽으로 좁혀짐
        else:
            right = mid - 1 # 검색 범위가 왼쪽으로 좁혀짐

    return False

n, m = map(int, input().split())
n_list = [input() for _ in range(n)]
m_list = [input() for _ in range(m)]

n_list.sort()

cnt = 0
for prefix in m_list:
    if binary_search(n_list, prefix):
        cnt += 1

print(cnt)

# 시간초과
n, m = map(int, input().split())

n_list = [input() for _ in range(n)]
m_list = [input() for _ in range(m)]
	
def prefix(n_list, m_list):
	cnt = 0
	
	for i in m_list:
		for j in n_list:
			if j.startswith(i):
				cnt += 1
				break
	
	return cnt

print(prefix(n_list, m_list))