## 题目：学术交流
## 类型：

## 题目描述：要求任意两个人都能直接或者间接地交流
## 输入：
# 3 3 2（3个人、3种语言、能获取以下两条信息）
# 2 3（第二个人会第三种语言）
# 3 1（第三个人会第一种语言）
# 输出：
# 2（需要2个学习机）

## 思路：在没有任何信息的条件下，n个人n种语言，每个人语言不同，则需要n-1台学习机；假设信息中给定了sameNum个人会同一种语言，则可以少负担sameNum个学习机，因此最终为=需要n-sameNum-1个学习机。
## 思路二：此题需要考虑图算法，利用深度优先搜索的算法进行求解。

def getNum(res, k, n):
    sameNum = k - len(set(res))
    return n-sameNum-1


if __name__ == "__main__":
    n,m,k = list(map(int, input().split()))
    Arr = []
    res = []
    for i in range(k):
        Arr.append(list(map(int, input().split())))
        res.append(Arr[i][1])

    num = getNum(res,k,n)
    print(num)
        

