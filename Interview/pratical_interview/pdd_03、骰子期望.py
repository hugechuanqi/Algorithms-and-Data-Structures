## 题目：骰子期望
## 类型：动态规划

## 题目描述：
## 输入：
## 输出：

## 核心：
## 思路：


n = int(input())#多少骰子
nums = list(map(int,input().split()))#每个骰子的可能结果数
 
ans = [[0 for i in range(51)] for j in range(50)]#初始化结果
maxnum = 0
for x in range(1,nums[0]+1):#初始化第1次的结果
    ans[0][x] = 1
    maxnum = max(maxnum,nums[0])
for i in range(1,n):#每个骰子
    maxnum = max(maxnum,nums[i])
     
    for j in range(1,maxnum+1):#可能的取值
        if nums[i]>=j:#如果当前数值小于当前能取到的最大值
            ans[i][j] = sum(ans[i-1][:j+1])+(j-1)*ans[i-1][j]
        else:#如果当前数值大于当前能取到的最大值
            ans[i][j] = ans[i-1][j] * nums[i]
         
all_ = 0
all_num = 0
for i in range(1,51):
    all_ += ans[n-1][i]
    all_num += ans[n-1][i]*i
print ('%.2f'%(all_num/all_))