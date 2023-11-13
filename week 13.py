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