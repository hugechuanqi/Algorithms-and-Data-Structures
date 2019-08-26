## 俄罗斯方块
## 类型：数组，贪心

## 题目描述："请输入荧幕列数n，方格块数m："，并输入m个"请输入方格依次落下的位置C："，当所有列都满格时，得一分。

# 思路：这道题的思路很简单，N列，就定义一个1*N的数组，每一列落下方块时，对应数组位置+1，最后取数组的最小值就可以了


def getNum(n, c):
    a = [0 for i in range(n)]
    for i in c :
        a[i-1] += 1 # 出现几次就叠加几次
        pass
    return  min(a)

if __name__ == "__main__":
    n, m = list(map(int,  input().split()))
    c = list(map(int,  input().split()))
    num = getNum(n, c)
    print(num)

## 测试用例
#输入：
#3 9
#1 1 2 2 2 3 1 2 3
#输出：
#2