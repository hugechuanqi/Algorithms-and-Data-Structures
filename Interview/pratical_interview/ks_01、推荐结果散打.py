## 题目：
## 类型：推荐系统图片打散

## 题目描述：

## 核心：如何pop之后保证字符串的长度不变，或者说如何取值非连续的3个字符出来——计算出来比较复杂，先放着
## 思路：

# class Solution:
#     def changePicture(self, data, N):
#         i = 0
#         queue = []
#         while(i+N-1<len(data)):
#             count = 0
#             for low in range(i, i+N):
#                 if data[low]=='P':
#                     count += 1
#                 if count==2:
#                     queue = data.pop(low)
#                     break
#                 if count==0 and low==i+N-1 and data[low]=='V' and len(queue)>0:
#                     a = queue.pop(0)
#                     data.insert(low, a)
#             i = low
#         return data

# if __name__ == "__main__":
#     N = int(input())
#     M= int(input())
#     data = []
#     for i in range(M):
#         s = input()
#         data.append(s)
#     a = Solution()
#     data1 = a.changePicture(data, N)
#     length = len(data1)
#     print(length)
#     for i in range(length):
#         print(data1[i])


import sys
 
data = []
for line in sys.stdin.readlines():
    data.append(line.strip())
 
N = int(data[0])
M = int(data[1])
 
if M == 1:
    print(1)
    print(data[2])
elif N == 1:
    print(M)
    for x in data[2:]:
        print(x)
else:
    res = []
    P = []
    V = []
    ptr = -1
    for i, x in enumerate(data[2:]):
        if x[0] == 'V':
            res.append(x)
        else:
            res.append(x)
            ptr = i
            break
    if ptr == -1:
        print(M)
        for x in res:
            print(x)
    else:
        for x in data[ptr+2:]:
            if x[0] == 'P':
                P.append(x)
            else:
                V.append(x)
        P = P[1:]
 
        while V:
            if len(V) >= N-1:
                res += V[:N-1]
                V = V[N-1:]
                if P:
                    res.append(P[0])
                    P = P[1:]
                else:
                    res += V
                    break
            else:
                res += V
                break
        print(len(res))
        for x in res:
            print(x)

## 测试用例：
## 输入：
# 3
# 10
# V_0
# V_1
# V_2
# P_3
# V_4
# P_5
# P_6
# V_7
# V_8
# V_9
## 输出：
# 9
# V_0
# V_1
# V_2
# P_3
# V_4
# V_7
# P_5
# V_8
# V_9
