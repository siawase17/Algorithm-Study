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