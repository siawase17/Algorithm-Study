# 11501번: 주식 (그리디)
t = int(input())

def max_profit(t):
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        current = arr[n - 1]
        profit = 0

        for i in range(n - 2, -1, -1):
            if current < arr[i]:
                current = arr[i]
                continue
            profit += current - arr[i]

        print(profit)

max_profit(t)

# 2141번: 우체국 (그리디)
n = int(input())
town = [] # (위치, 인구)
population = 0  # 전체 인구 수

# 각 마을 정보 입력 및 전체 인구 수 누적
for _ in range(n):
    pos, p = map(int, input().split())
    town.append((pos, p))
    population += p

# 마을을 위치를 기준으로 정렬
town.sort()

# 전체 인구 수의 중앙 위치 구하기
mid_population = (population + 1) // 2

# 인구의 절반이 속한 마을에 우체국 설치
cur_population = 0
for loc, p in town:
    cur_population += p

    if cur_population >= mid_population:
        print(loc)
        break

####### 아래는 함수 풀이 ###########

def find_location(town):
    population = sum(map(lambda x: x[1], town)) # 전체 인구 수
    town.sort() # 마을을 위치를 기준으로 정렬

    # 전체 인구 수의 중앙 위치 구하기
    mid_population = (population + 1) // 2

    # 인구의 절반이 속한 마을에 우체국 설치
    cur_population = 0
    for loc, p in town:
        cur_population += p

        if cur_population >= mid_population:
            return loc

n = int(input())
town = [] # (위치, 인구)

# 각 마을 정보 입력
for _ in range(n):
    pos, p = map(int, input().split())
    town.append((pos, p))

result = find_location(town)
print(result)




