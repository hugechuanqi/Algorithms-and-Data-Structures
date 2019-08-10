
def CountNumber(n_num, left, right):
        if left > right:
                return 0
        n_num.sort()
        if n_num[0] > right:
                return 0
        if n_num[-1] < left:
                return 0
        count = 0                        
        for elem in n_num:
                if left <= elem <= right:
                        count += 1
        return count

T = int(input())
for i in range(T):
        print("Case #%d:" %(i+1))
        n, m = list(map(int, input().split()))
        n_num = list(map(int, input().split()))
        for i in range(m):
                left, right = list(map(int, input().split()))
                # print("区间：", left, right)
                num = CountNumber(n_num, left, right)
                print(num)


T = int(input())
nums = [[0]]*T
for i in range(T):
        nums[i] = []
        n, m = list(map(int, input().split()))
        n_num = list(map(int, input().split()))
        for j in range(m):
                left, right = list(map(int, input().split()))
                num = CountNumber(n_num, left, right)
                nums[i].append(num)
for i in range(T):
        print("Case #%d:" %(i+1))
        for num in nums[i]:
                print(num)
   

## 测试用例：
# 输入：
# 2
# 10 5
# 0 1 2 3 4 5 6 7 8 9
# 0 5
# 10 20
# -5 -3
# 7 7
# 100 105
# 5 1
# 1 1 1 1 1
# 0 2
# 输出：
# Case #1:
# 6
# 0
# 0
# 1
# 0
# Case #2:
# 5
