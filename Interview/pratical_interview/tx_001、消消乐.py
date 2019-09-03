## 题目：消消乐

def checkRemove(Arr):
    count ={}
    max_value = 0
    for i in set(Arr):
        a = Arr.count(i)
        count[i]= a
        if a>max_value:
            max_value = a

    if len(Arr)-max_value>=max_value:
        return True
    else:
        return False

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        length = int(input())
        Arr = list(map(int, input().split()))
        Arr.sort(reverse=True)
        if checkRemove(Arr):
            print("YES")
        else:
            print("NO")

## 测试用例：
# 输入：
# 1
# 6
# 1 2 3 4 5 6
# 输出：
# YES


##  1、消消乐——只计算最多的那个数60%
## 2、花匠小Q
## 3、猜硬币（完全不明白输出的意思）
## 4、复读——完成，就是时间复杂度有点大70%
## 5、小Q的矩形


