# 프로그래머스: 광물캐기 (백트래킹)
price = [[1,1,1],[5,1,1],[25,5,1]]
pick = {"diamond":0, "iron":1, "stone":2}

def solution(picks, minerals):
    picks = sum([[idx]*val for idx, val in enumerate(picks)], [])
		# picks = [1, 2]
		# sum 빼니까 pick = [[], [1], [2]] 되고 최종 출력은 오류 뜸
    
    minerals = [pick[i] for i in minerals[:5*sum(picks)]]
    
    processed = sorted([minerals[i:i+5] for i in range(0, len(minerals), 5)], key=lambda x:-sum([price[2][i] for i in x]))
    
    return sum([sum([price[picktype][i] for i in items]) for picktype, items in zip(picks, processed)])

# 프로그래머스: 소수찾기 (백트래킹)
import itertools
def solution(numbers):
    answer = 0
    new=[]
    for i in range(1,len(numbers)+1): 
        for permutation in itertools.permutations(numbers, i): # (리스트, 순열길이)
            new.append(int("".join(permutation)))
            
    for i in set(new):
        is_prime = True
        if i < 2:
            continue
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1
                
    return answer

# 프로그래머스: 타겟넘버 (백트래킹)
def solution(numbers, target):

    def dfs(index, current_sum):
        if index == len(numbers): # 모든 숫자 처리
            return 1 if current_sum == target else 0

        positive_count = dfs(index + 1, current_sum + numbers[index])
        negative_count = dfs(index + 1, current_sum - numbers[index])

        return positive_count + negative_count

    answer = dfs(0, 0)
    return answer