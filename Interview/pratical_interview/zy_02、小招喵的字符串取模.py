## 题目：小招喵的字符串取模（10%）
## 类新：数字规律

def checkNum(strs, stack):
    length = len(stack)
    if len(strs)!=length:
        strs = 'a'*(length-len(strs)) +strs
    for i in range(length):
        if stack[i]!='a' and stack[i]!=strs[i]:
            return False
    return True  

def countNum(minNum, maxNum,stack):
    count = 0
    res = []
    for i in range(minNum, maxNum+1):
        if checkNum(str(i), stack):
            
            if i-5>=0 and (i-5)%13==0:
                res.append(i)
                count += 1
    # print(res, len(res))
    return count

def numRange(strs):
    stack = []
    minNum = ''
    maxNum = ''
    for elem in strs:
        if elem=="?":
            stack.append('a')
            maxNum = maxNum + '9'
            if minNum != '':
                minNum = minNum + '0'
        else:
            stack.append(elem)
            maxNum += elem
            minNum += elem
    count = countNum(int(minNum), int(maxNum), stack)
    return count

if __name__ == "__main__":
    strs = input()
    MOD = 10**9+7
    count = numRange(strs)
    print(count%MOD)

## 测试用例：
# 输入：2?? -> 200~299
# 输出：8
# 输入：???5 -> 0005~9995
# 输出：77


