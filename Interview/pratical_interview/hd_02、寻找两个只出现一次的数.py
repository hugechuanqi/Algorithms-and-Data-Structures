## 题目：寻找两个只出现过一次的数
## 类型：数组

## 题目描述：2n+2个数,有n个出现两次,要求输出安大小顺序输出剩余两个只出现一次的值

## 思路：

def getNum(Arr):
    res = []
    for elem in Arr:
        if elem not in res:
            res.append(elem)
        else:
            res.remove(elem)
    return sorted(res)

if __name__ == "__main__":
    n = int(input())
    Arr = list(map(int, input().split()))
    res = getNum(Arr)
    print(res[0],  res[1])

## 测试用例：
# 输入：
# 8
# 1 2 3 4 5 1 2 5
# 输出：
# 3 4
