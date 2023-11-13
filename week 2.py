# 10988번: 팰림드롬인지 확인하기
def isPalindrome(text):
    if text == text[::-1]:
        return 1
    else:
        return 0

text = input()
result = isPalindrome(text)
print(result)