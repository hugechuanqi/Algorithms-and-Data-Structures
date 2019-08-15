def solve(str):
    length = len(str)
    totalList = []
    totalNumber = 0
    i = 0
    temp = ''  # 暂存一个字符串
    while i < length:
        s = str[i]
        if s != ',' and s != '"':
            temp = temp + s
            i = i + 1
        elif s == ',':
            totalNumber = totalNumber + 1
            totalList.append(temp)
            temp = ''
            i = i + 1
        else:
            x = i + 1#x表示字符串当前字符位置
            while x < length:
                if x + 1 == length and str[x] == '"':
                    i = x + 1
                    break
                elif str[x] == '"' and str[x + 1] == '"':
                    temp = temp + '"'
                    x = x + 2
                elif str[x] == '"':
                    print('ERROR')
                    return
                else:
                    temp = temp + str[x]
                    x = x + 1
            if x == length:
                print('ERROR')
                return
    totalList.append(temp)
    print(len(totalList))
    # for j in range(len(totalList)):
    #     print(totalList[j])

    return

if __name__ == '__main__':
    # str = 'a,,1,"b,"""'
    strs = input()
    solve(strs)

## 测试用例：
# 输入：
# a,,1,"b,"""
# 输出：
# 4
