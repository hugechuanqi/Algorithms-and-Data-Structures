## 类型：贪心算法
## 题目做出来了，可惜已经提交了
class Solution:
    def leastTime(self, strs, flag):
        if len(strs)==0:
            return 0
        if flag == 0:
            if strs[0][0] > strs[0][1] + strs[0][2]:
                res =  strs[0][1] + strs[0][2] + self.leastTime(strs[1:], 1)
            else:
                res =  strs[0][0] +  self.leastTime(strs[1:], 0)
        elif flag == 1:
            if strs[0][1] > strs[0][0] + strs[0][2]:
                res = strs[0][0] + strs[0][2] + self.leastTime(strs[1:], 0)
            else:
                res =  strs[0][1] +  self.leastTime(strs[1:], 1)
        return res

n = int(input())
strs = []
for i in range(n):
    string_ = list(map(int, input().split()))
    strs.append(string_)
print(strs)
a = Solution()
res = a.leastTime(strs, flag=1)
print(res)

## 输入：
# 3
# 20 40 20
# 10 4 25
# 90 100 5
## 输出：
# 139

