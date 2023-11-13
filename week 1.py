# 1343번: 폴리오미노
'''
- 인덱스가 문자열의 길이를 넘지 않을 때까지 while문 반복
- 조건문을 이용해 XXXX와 XX의 경우를 나누었음
- 조건이 맞는다면 변환 후 인덱스 증가.
- XXXX와 XX의 조건을 둘 다 만족하지 못하면 변환할 수 없는 문자열이므로 -1 리턴
- ‘.’을 만난 경우는 변환이 필요 없으므로 인덱스만 증가
- 문자열 길이보다 i값(인덱스)이 커지면 결과 리턴
'''
def polyomino(board):
    i = 0  # 문자열 인덱스
    while i < len(board):
        if board[i] == 'X':  # 'X'를 찾으면
            if board[i+1:i+4] == 'XXX':  # 'XXXX'일 경우
                board = board[:i] + 'AAAA' + board[i+4:]
                i += 4
            elif board[i+1:i+2] == 'X':  # 'XX'일 경우
                board = board[:i] + 'BB' + board[i+2:]
                i += 2
            else:  # 변환할 수 없는 경우
                return "-1"
        else: # 인덱스값 . 인 경우
            i += 1
    return board

board = input()
result = polyomino(board)
print(result)

# 10994번: 별찍기
def star_line(n, i):
    a = 4 * (n-i) + 1
    stars = '*' * a
    print('* ' * (i-1) + stars + ' *' * (i-1))
    
def space_line(n, i):
    a = 4 * (n-i) + 1
    spaces = ' ' * (a-4)
    print('* ' * i + spaces + ' *' * i)

def star_pattern(n):
    for i in range(1, n):
        star_line(n, i)
        space_line(n, i)
    print('* ' * (n * 2 - 1))
    for i in range(n-1, 0, -1):
        space_line(n, i)
        star_line(n, i)

n = int(input())
star_pattern(n)