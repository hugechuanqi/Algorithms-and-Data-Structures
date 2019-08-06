# n = int(input())
# a=[]
# for i in range(n):
#     a.append(int(input()))
# amin = min(a)
# amax = max(a)
# flag = 0
# if amax-amin==0:
#     print(0)
# else:
#     while(amax-amin!=0):
#         for i in range(n):
#             if a[i]%amin!=0 or a[i]>amin:
#                 a[i] = a[i] / 2
#                 flag = flag + 1
#             else:
#                 continue
#         amax = max(a)
#         amin = min(a)
#     print(flag)

# a1 = 1
# a2 = 2
# a3 = 4

import math
n = int(input())
a_input = input().split()
a = [0 for i in range(n)]
counter = [0 for i in range(n)]
counter_sum = 0
for i in range(n):
    num = int(a_input[i])
    while math.log(num,2)%1 != 0:
        num = math.floor(num/2)
        counter[i] += 1
    num = math.log(num,2)
    a[i] = int(num)
ave = round(sum(a)*1.0/n)
print(a)
for i in range(n):
    counter_sum += abs(a[i]-ave)
print(counter_sum+sum(counter))

