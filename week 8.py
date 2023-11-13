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