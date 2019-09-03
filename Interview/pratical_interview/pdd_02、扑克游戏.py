## 题目：扑克游戏
## 类型：深度优先搜索
# 参考：https://www.nowcoder.com/discuss/241378?type=post&order=time&pos=&page=1

## 题目描述：小三和小舞玩扑克牌，每一局，
## 输入：
## 输出：

## 核心：
## 思路：


s = int(input())
def cmp(s1,s2):
    if len(s1)!=len(s2):
        return False
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            return False
    return True
for i in range(s):
    nums = [char for char in input()]
    news = [char for char in input()]
    n = len(nums)
    paths = []
    def search(nums,luans,news,path,n):
        if n == 0:
            if cmp(luans,news):
                paths.append(path)
            return
        num = nums[0]
        nums = nums[1:]
        search(nums,luans,news,path+['d'],n-1)
        search(nums,[num]+luans,news,path+['l'],n-1)
        search(nums,luans+[num],news,path+['r'],n-1)
    search(nums,[],news,[],n)
    print ('{')
    for path in paths:
        print (' '.join(path))
    print ('} ')

