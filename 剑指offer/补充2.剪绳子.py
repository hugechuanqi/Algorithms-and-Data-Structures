# 剪绳子
class Solution:
    ## 动态规划算法，计算出每个长度的绳子剪掉之后的长度最大值
    def maxProductAfterCutting(self,length):
        if length<2:
            return 0
        if length==2:
            return 1
        if length==3:
            return 2

        product = [0]*(length+1)  #注意这里数组从0开始，因此乘积长度始终+1
        print("绳子初始乘积为：",product)
        product[0] = 0
        product[1] = 1
        product[2] = 2
        product[3] = 3
        for i in range(4,length+1):             #i表示从4开始到绳子长度的每个乘积
            maxValue = 0
            for j in range(1,int(i/2)+1):
                tmp = product[j]*product[i-j]   #j表示截取位置
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
        if length - 3*timeOf3 == 1:
            timeOf3 -= 1
        timeOf2 = (length - 3*timeOf3)//2

        return (3**timeOf3) * (2**timeOf2)

while(1):
    try:
        length = int(input())
        a=Solution()
        product =  a.maxProductAfterCutting(length)
        product2 =  a.maxProductAfterCutting2(length)
        print("绳子长度为：", length, "，剪绳子得到的最大乘积为：", product2)
    except:
        break