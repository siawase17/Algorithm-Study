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
