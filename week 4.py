# 2003번: 수들의 합2
def count_sum(a, m):
    count = 0
    current_sum = 0
    prefix_sum = {0: 1}  # 누적합 저장

    for num in a:
        current_sum += num
        count += prefix_sum.get(current_sum - m, 0) 
        prefix_sum[current_sum] = 1
    return count

n, m = map(int, input().split())
a = list(map(int, input().split()))

result = count_sum(a, m)
print(result)

# 시간초과
n, m = map(int, input().split())
a = list(map(int, input().split()))

count = 0  # 경우의 수
prefix_sum = [0]  # 누적합 저장 리스트

# 누적합 계산
for num in a:
    prefix_sum.append(prefix_sum[-1] + num)

# 부분합이 M이 되는 경우 찾기
for i in range(1, n+1):
    for j in range(i, n+1):
        if prefix_sum[j] - prefix_sum[i-1] == m:
            count += 1

print(count)

# 4949번: 균형잡힌 세상
def is_balanced(text):
    stack = []
    opening = '([{'
    closing = ')]}'
    
    for char in text:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0:
                return False
            opening_bracket = stack.pop()
            if opening.index(opening_bracket) != closing.index(char):
                return False
    
    return len(stack) == 0


output = []
while True:
    input_str = input()
    if input_str == '.':
        break
    elif is_balanced(input_str):
        output.append("yes")
    else:
        output.append("no")

print("\n".join(output))
'''
1. for char in text: 주어진 문자열 text를 한 글자씩 순회
2. if char in opening: 현재 문자가 여는 괄호인지 확인, 여는 괄호라면 스택에 추가
3. elif char in closing: 현재 문자가 닫는 괄호인지 확인, 닫는 괄호라면 스택의 상태를 체크
4. if len(stack) == 0: 스택이 비어있는 경우, 닫는 괄호가 먼저 나온 것이므로 False를 반환
5. opening_bracket = stack.pop(): 스택이 비어있지 않은 경우, 스택에서 가장 최근에 추가된 여는 괄호를 꺼내옴
6. if opening.index(opening_bracket) != closing.index(char): 꺼내온 여는 괄호와 현재 닫는 괄호의 짝이 맞는지 확인, 짝이 맞지 않는 경우 False를 반환
7. return len(stack) == 0: 문자열을 모두 순회한 후에도 스택에 여는 괄호가 남아있는 경우 False를 반환
'''

# 1158번: 요세푸스 문제
def josephus(n, k):
    q = list(range(1, n+1))
    result = []
    j = 0

    while q:
        if len(q) == 1:  # q의 길이가 1인 경우
            result.append(str(q.pop()))
        else:
            j = (j + k - 1) % len(q)
            result.append(str(q.pop(j)))

    return f'<{", ".join(result)}>'

n, k = map(int, input().split())
result = josephus(n, k)
print(result)
