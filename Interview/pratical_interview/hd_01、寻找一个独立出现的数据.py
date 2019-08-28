## 题目：寻找一个独立出现的数据
## 类型：数组，栈

## 题目描述：2n+1个整数，n个数都是有两个，只有一个数是单个的，找出来

## 思路：建立一个数组，存储只出现过一次的整数，凡是出现过两次的都直接弹出。

def getNum(Arr):
    res = []
    for elem in Arr:
        if elem not in res:
            res.append(elem)
        else:
            res.remove(elem)
    return res[0]

if __name__ == "__main__":
    n = int(input())
    Arr = list(map(int, input().split()))
    res = getNum(Arr)
    print(res)

## 测试用例:
# 输入:
# 7
# 1 2 3 4 2 3 1
# 输出:
# 4
