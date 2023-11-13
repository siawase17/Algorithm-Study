# 5639번: 이진검색트리
numbers = []
while True:
    num = input()
    
    if not num:
        break
    
    numbers.append(int(num))
    
def postorder(arr):
    if not arr:
        return []
    
    root = arr[0]
    left = []
    right = []
    
    for i in arr[1:]:
        if i < root:
            left.append(i)
        else:
            right.append(i)
        
    left_postorder = postorder(left)
    right_postorder = postorder(right)
    
    return left_postorder + right_postorder + [root]

ans = postorder(numbers)
for i in ans:
	print(i)