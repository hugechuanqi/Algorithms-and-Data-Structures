# 剪绳子
class Solution:
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
            for j in range(1,int(i/2)):
                tmp = product[j]*product[i-j]   #j表示截取位置
                if maxValue<tmp:
                    maxValue=tmp
                product[i]=maxValue
        
        maxValue = product[length]
        return maxValue

length = 4
a=Solution()
print("剪绳子得到的最大乘积为：", a.maxProductAfterCutting(length))
