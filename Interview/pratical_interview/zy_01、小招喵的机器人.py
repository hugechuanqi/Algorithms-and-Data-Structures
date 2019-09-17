## 题目：小招喵的机器人（20%）
## 类型：字符串，栈

## 题型：
## 思路：首先初始化数轴上每一个数据为1，然后从左往右数，凡是左侧右侧都是'R'，则当前机器人数量为0，再从右往左数，凡是左侧右侧都是'L'，则当前机器人数量为0。

def printstack(stack, num):
    res = [0]*num
    for i in range(num):
        if stack[i]=="L":
            break
    res[i-1] = num//2
    res[i] = num - num//2
    return res

def getRobortNum(strs):
    length = len(strs)
    res = []

    nums = []
    stack = []
    for elem in strs:
        if elem=='R':
            if not stack or stack[-1]=='R':
                stack.append(elem)
            elif stack[-1]=='L':
                num = len(stack)
                nums.append(num)
                res1 = printstack(stack, num)
                res.extend(res1)
                stack = []
                stack.append(elem)
        elif elem=='L':
            if not stack:
                print('error')
            else:
                stack.append(elem)
    num = len(stack)
    nums.append(num)
    res1 = printstack(stack, num)
    res.extend(res1)
    return res

if __name__ == "__main__":
    strs = input()
    res = getRobortNum(strs)
    res = map(str, res)
    print(' '.join(res))

## 测试用例：
# 输入：
# RRLLRRLRRRLL
# 输出
# 022001200230
#RRL->012, RRLL->0220,RLRL->11111
