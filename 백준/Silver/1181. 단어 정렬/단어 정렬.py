N = int(input())

words = set()  # 중복된 단어를 제거하기 위해 set 사용
for _ in range(N):
    word = input().strip()  # 문자열의 양 끝에 있는 공백 제거
    words.add(word)

# 선택 정렬을 사용하여 정렬
sorted_words = list(words)
for i in range(len(sorted_words)):
    min_idx = i
    for j in range(i+1, len(sorted_words)):
        # 길이를 기준으로 정렬하고, 길이가 같은 경우에는 사전 순으로 정렬
        if len(sorted_words[j]) < len(sorted_words[min_idx]) or (len(sorted_words[j]) == len(sorted_words[min_idx]) and sorted_words[j] < sorted_words[min_idx]):
            min_idx = j
    sorted_words[i], sorted_words[min_idx] = sorted_words[min_idx], sorted_words[i]

for word in sorted_words:
    print(word)
