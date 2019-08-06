# s是否能构成环（中间数必须小于两边数的和）

time = map(int, input().split())
n = list(map(int, input().split()))[0]
array = list(map(int, input().split()))

flag = True
for i in range(n):
    value = array[i]
    if i ==0:
        if value > array[1]+array[n-1]:
            flag = False
    elif i==n-1:
        if value > array[n-2] + array[0]:
             flag = False
    else:
        if value > array[i-1] + array[i+1]:
             flag = False
if flag:
    print("YES")
else:
    print("NO")

        

# min_value = min(array)
# max_value = max(array)
# array_second = []
# for value in array:
#     if value != min_value:
#         array_second.append(value)
# second_min_value = min(array_second)

# if max_value > min_value + second_min_value:
#     print("NO")
# else:
#     print("YES")

