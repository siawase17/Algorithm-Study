# 프로그래머스: 전화번호 목록
def solution(phone_book):
    answer = True
    sorted_book = sorted(phone_book)
    
    for i in range(len(sorted_book) - 1):
        if sorted_book[i] == sorted_book[i+1][:len(sorted_book[i])]:
            return False

    return answer
'''
sorted_book = phone_book.sort()
sort() 메서드는 리스트를 정렬한 후 리스트 자체를 반환하지 않고 None을 반환. 
따라서 sorted_book에 None이 들어가게 되고, 이후 슬라이싱이나 길이 구하는 연산을 수행할 때 TypeError 발생.
'''

# 프로그래머스: 주식가격
def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break

    return answer

'''
prices = [1, 2, 3, 2, 3]

i = 0일 때:
j = 1, prices[0] = 1, prices[1] = 2 => answer = [1, 0, 0, 0, 0]
j = 2, prices[0] = 1, prices[2] = 3 => answer = [2, 0, 0, 0, 0]
j = 3, prices[0] = 1, prices[3] = 2 => answer = [3, 0, 0, 0, 0]
j = 4, prices[0] = 1, prices[4] = 3 => answer = [4, 0, 0, 0, 0]

i = 1일 때:
j = 2, prices[1] = 2, prices[2] = 3 => answer = [4, 1, 0, 0, 0]
j = 3, prices[1] = 2, prices[3] = 2 => answer = [4, 2, 0, 0, 0]
j = 4, prices[1] = 2, prices[4] = 3 => answer = [4, 3, 0, 0, 0]

i = 2일 때:
j = 3, prices[2] = 3, prices[3] = 2 => answer = [4, 3, 1, 0, 0]

i = 3일 때:
j = 4, prices[3] = 2, prices[4] = 3 => answer = [4, 3, 1, 1, 0]

마지막 값은 무조건 0
'''

