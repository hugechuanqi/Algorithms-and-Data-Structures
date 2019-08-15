## 题目：字符串逗号分隔存储
## 类型：字符串

## 要求：
## 输入：存储的字符串
## 输出：该字符串的字段个数

## 核心：无法直接使用一个指针来实现，因为当遇到双引号'"'时，我们不确定之后的字符串会有多长，因此需要另一个指针取探测。

## 错误事例
def getFiledNum(strs):
    res = []
    temp = ""
    i, j = 0, 0
    while(i<len(strs)):
        if strs[0]==',' or strs[-1]==',':
            print("ERROR")
            return
        if strs[i] != ',' and strs[i] != '"':
            temp += strs[i]
            i += 1
        elif strs[i] == '"':
            if i == len(strs)-1:
                print("ERROR")
                return
            j = i + 1
            while(j<len(strs)):
                print(i, j)
                if j+1 == len(strs) and strs[j]=='"':
                    j = j + 1
                    i = j + 1
                    break
                elif strs[j]=='"' and strs[j+1]=='"':
                    temp += strs[j+1]
                    j = j+2
                    i = j
                elif strs[j]=='"' and strs[j+1]!=',':
                    print("ERROR")
                    return 
                else:
                    temp += strs[j]
                    j = j + 1
                    i = j
        else:
            res.append(temp)
            temp = ''
            i = i + 1
    res.append(temp)
    print(len(res))
    return

strs = input()
getFiledNum(strs)


## 测试用例：
# 输入：
# a,,1,"b,"""
# 输出：
# 4
# 输入：
# ,a,,1,"b,"""
# 输出：
# ERROR
# 输入：
# a,,12,"b,""""
# 输出：
# ERROR
