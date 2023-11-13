# 10988번: 팰림드롬인지 확인하기
def isPalindrome(text):
    if text == text[::-1]:
        return 1
    else:
        return 0

text = input()
result = isPalindrome(text)
print(result)

# 18311번: 왕복
n, k = map(int, input().split())
course = list(map(int, input().split()))
return_course = course + course[::-1]

a = 0
for i in range(n * 2):
    a += return_course[i]
    if a > k:
        break
        
print(i+1 if i < n else 2*n - i)