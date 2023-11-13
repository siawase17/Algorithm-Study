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