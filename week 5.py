# 9251번: LCS
def LCS(x, y):
    n = len(x)
    m = len(y)
    
    dp_table = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(1, n+1): # 인덱스 0은 초기화를 위해 사용
        for j in range(1, m+1):
            if x[i-1] == y[j-1]: # 인덱스는 0부터 시작하므로 i와 j를 각각 i-1, j-1로 수정
                dp_table[i][j] = dp_table[i-1][j-1] + 1
            else:
                dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])
    
    return dp_table[n][m]

x = input()
y = input()

print(LCS(x, y))

# 2578번: 빙고
def bingo(arr, nums):
	# 세로 (전치, 행을 열로 열을 행으로)
	vertical_lines = list(map(list, zip(*arr)))
	# 대각선
	diagonal1 = []
	diagonal2 = []
	for i in range(5):
	    diagonal1.append(arr[i][i])
	    diagonal2.append(arr[i][4-i])
	
	# 빙고판의 전체(가로, 세로, 대각선)
	data = arr + vertical_lines + [diagonal1] + [diagonal2]
	
	for num in nums:
	    for i in range(12): # 인덱스) 가로 0-4, 세로 5-9, 대각선1 10, 대각선2 11
	        for j in range(5):
	            if data[i][j] == num:
	                data[i][j] = 0
	
	    bingo = data.count([0, 0, 0, 0, 0])
	
	    if bingo >= 3:
	        result = nums.index(num)
	        break
	
	return result + 1

arr = [list(map(int, input().split())) for _ in range(5)]
# 사회자가 부르는 숫자 (하나의 리스트로 저장)
nums = [int(x) for _ in range(5) for x in input().split()]

print(bingo(arr, nums))