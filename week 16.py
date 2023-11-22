# 11501번: 주식 (그리디)

t = int(input())
def max_profit(t):
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.reverse()
        current = arr[0]
        profit = 0

        for i in range(1, n):
            if current < arr[i]:
                current = arr[i]
                continue
            profit += current - arr[i]

        print(profit)

max_profit(t)



