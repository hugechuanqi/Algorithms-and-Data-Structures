## 题目：锯木棍
## 类型：动态规划

def maxProductAfterCutting(length):
        if length<2:
            return 0
        if length==2:
            return 1
        if length==3:
            return 2

        product = [0]*(length+1)
        product[0] = 0
        product[1] = 1
        product[2] = 2
        product[3] = 3
        for i in range(4,length+1):
            maxValue = 0
            for j in range(1,int(i/2)+1):
                tmp = product[j]*product[i-j]
                if maxValue<tmp:
                    maxValue=tmp
                product[i]=maxValue
        
        maxValue = product[length]
        return maxValue

n = int(input())
num = maxProductAfterCutting(n)
print(num)