from PIL import Image
from io import BytesIO
import requests

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
# 시간 초과
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

# 설명 이미지
img_url = 'https://file.notion.so/f/s/775a50ee-938f-4a66-be35-8261434ccae5/Untitled.png?id=3375fd65-a0f9-4409-ac3a-8990b1447640&table=block&spaceId=19f14110-c29c-496f-9b95-062969c86b08&expirationTimestamp=1700006400000&signature=uAH2fEiXgdRam83AAC_msOhUXGfyD5rjjuetwKpm44E&downloadName=Untitled.png'
response = requests.get(img_url)
image = Image.open(BytesIO(response.content))
image.show()

