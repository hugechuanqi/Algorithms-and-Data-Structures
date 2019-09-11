## 题目：训练部队
## 类型：贪心算法

## 题目描述：小牛牛是牛牛王国的将军,为了训练出精锐的部队,他会对新兵进行训练。部队进入了n个新兵,每个新兵有一个战斗力值和潜力值,当两个新兵进行决斗时,总是战斗力值高的获胜。获胜的新兵的战斗力值就会变成对手的潜力值 + 自己的战斗力值 - 对手的战斗力值。败者将会被淘汰。若两者战斗力值一样,则会同归于尽,双双被淘汰(除了考察的那个新兵之外，其他新兵之间不会发生战斗) 。小牛牛想知道通过互相决斗之后新兵中战斗力值+潜力值最高的一个可能达到多少,你能帮助小牛牛将军求出来吗?

## 输入：输入包括n+1行,第一行包括一个整数n(1 ≤ n ≤ 10^5);接下来的n行,每行两个整数x和y(1 ≤ x,y ≤ 10^9)
## 输出：输出一个整数,表示新兵中战斗力值+潜力值最高的一个能达到多少。

## 核心：贪心算法+求最大战力潜力和+求潜力战力差之和
## 思路：已知获胜战斗力值会加上对手的潜力值-对手的战斗力值。
# 贪心思想，要培养一个战力潜力和最大的兵王，就要尽可能多的增加其战力，即打赢所有潜力大于战力的新兵，记他们的潜力战斗差的总和为add。有两种情况：
#   1、潜力qian大于战力zhan，不能与自己交战，所以要先从add中减去他的部分，最终兵王战力潜力和为add-(qian-zhan)+zhan+qian=add+2*zhan 
#   2、否则，直接加上他的潜力战力，即add+qian+zhan。
# 故对两种情况，分别找到战力最大值maxZhan与潜力战力和的最大值maxSum，比较2*maxZhan和maxSum, 取大的加上add即为正确答案 


class Solution:
    def HighValue(self, length, Arr):
        """ 贪心算法：兵王
        """
        maxZhan, add, maxSum = 0, 0, 0  # 含义：最大战力，潜力战力差总和，
        for i in range(length):
            zhan = Arr[i][0]
            qian = Arr[i][1]
            if qian>zhan:
                maxZhan = max(maxZhan, zhan)
                add += qian-zhan
            else:
                maxSum = max(maxSum, zhan+qian)
        res = add+max(2*maxZhan, maxSum)
        return res

if __name__ == "__main__":
    length = 2
    Arr = []
    # for i in range(length):
    Arr.append([1,2])
    Arr.append([2,1])
    a = Solution()
    print(a.HighValue(length, Arr))

## 测试用例：
# 输入：
# 2
# 1 2
# 2 1
# 输出：
# 4
