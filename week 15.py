# 12847번: 꿀아르바이트
n, m = map(int, input().split())
pay = list(map(int, input().split()))

def maximum_profit(n, m, pay):
    max_profit = sum(pay[:m])
    current_profit = max_profit

    for i in range(m, n):
        current_profit = current_profit - pay[i - m] + pay[i]
        max_profit = max(max_profit, current_profit)

    return max_profit

result = maximum_profit(n, m, pay)
print(result)





