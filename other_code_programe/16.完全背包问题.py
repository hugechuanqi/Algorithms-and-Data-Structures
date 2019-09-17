## 题目：背包问题
## 类型：贪心算法，动态规划

## 题目描述：有N种物品和一个容量为V的背包，每种物品都有无限件可用。第i种物品的体积是vi，价值是wi，求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。输出最大价值。
# [背包九讲](https://www.cnblogs.com/jbelial/articles/2116074.html)
# [acwing练题网站](https://www.acwing.com/problem/content/3/)

class Solution:
    def getdict(self, Volume, value):
        VolumeValue = {}
        for i in range(len(Volume)):
            key = Volume[i]
            if key not in VolumeValue.keys():
                VolumeValue[key] = value[i]
            elif value[i] > VolumeValue[key]:
                VolumeValue[key] = value[i]
            else:
                continue
        return VolumeValue

    def BagMaxValue(self, num, VolumeLimit,  Volume, value):
        VolumeValue = a.getdict(Volume, value)
        print("物品体积价值对应比：", VolumeValue, list(VolumeValue.items()))

        Volume = list(VolumeValue.keys())
        value = list(VolumeValue.values())
        print(Volume, value)

        rows = VolumeLimit
        cols = len(Volume)
        dp = [0 for i in range(VolumeLimit)]
        for i in range(1, VolumeLimit):
            for j in VolumeValue:
                if j<=i:
                    dp[i] = max(dp[i], dp[i-j]+value[j])
        return dp

if __name__ == "__main__":
    # 1、完全背包问题
    num = 6         # 物品数量
    VolumeLimit = 10        # 书包能承受的体积
    Volume = [2,2,3,1,5,2]     # 每个物品的体积
    value = [2,3,1,5,4,3]         # 每个物品的价值
   
    a = Solution()
    dp = a.BagMaxValue(num, VolumeLimit, Volume, value)
    print("背包最大价值为：", dp[VolumeLimit-1])




