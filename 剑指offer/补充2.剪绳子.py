## 题目：剪绳子
## 类型：动态规划，贪心算法

## 题目描述：给你一根长度为n的绳子，请把绳子剪成m段，每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0] x k[1] x ... x k[m]可能的最大乘积是多少？
## 输入：8
## 输出：18=3*3*2

## 思路：动态规划——自下而上，子问题的最优解存储在数组products中，数组中第i个元素表示长度为i的绳子剪成若干段之后，各段长度乘积的最大值。贪心算法——


class Solution:
    ## 动态规划算法，计算出每个长度的绳子剪掉之后的长度最大值
    def maxProductAfterCutting(self,length):
        """ 动态规划：自下而上，每次将最优解存储在数组products中，每次剪绳子都去之间的最大值
        """
        if length<2:
            return 0
        if length==2 or length==3:      #2=1*1, 3=2*1
            return length-1
        product = [0]*(length+1)  #注意这里数组从0开始，因此乘积长度始终+1
        product[0] = 0
        product[1] = 1
        product[2] = 2
        product[3] = 3

        for i in range(4,length+1):             #i表示从4开始到绳子长度的每个乘积
            maxValue = 0
            for j in range(1,int(i/2)+1):   # 从0一直截取到绳子长度的一半，后续相当于重复，绳子最短长度为1，因此从1开始
                tmp = product[j]*product[i-j]   #j表示截取位置，每次的截取都去之前剪绳子长度的最大值
                if maxValue<tmp:
                    maxValue=tmp
                product[i]=maxValue
        
        maxValue = product[length]
        return maxValue

    ## 贪心算法，当n>=5时，计算长度为3的绳子的倍数；当n=4时，由于2*2 > 3*1，因此计算两个长度为2的绳子的倍数
    def maxProductAfterCutting2(self, length):
        if length < 2:
            return 0
        elif length == 2:
            return 1
        elif length == 3:
            return 2

        timeOf3 = length//3
        if length - 3*timeOf3 == 1:     # 即最后剪成的绳子是4=3+1，此时剪成4=2*2>3*1更好。
            timeOf3 -= 1
        timeOf2 = (length - 3*timeOf3)//2

        return (3**timeOf3) * (2**timeOf2)

if __name__ == "__main__":
    while(1):
        try:
            length = int(input())
            a=Solution()
            product =  a.maxProductAfterCutting(length)
            product2 =  a.maxProductAfterCutting2(length)
            print("绳子长度为：", length, "，剪绳子得到的最大乘积为：", product2)
        except:
            break