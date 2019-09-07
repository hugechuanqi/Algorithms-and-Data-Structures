## 插空
def check(i, Arr, length):
    if i-1<0 and i+1<=length-1:
        if Arr[i+1]==0:
            return True
    if i+1>=length and i-1 >=0:
        if Arr[i-1]==0:
            return True
    if i-1 >=0 and i+1<=length-1:
        # print(i-1, i+1, length-1, Arr[i+1])
        if Arr[i-1]==0 and Arr[i+1]==0:
            return True
    return False

def insertNum(length, Arr):
    count = 0
    for i in range(length):
        if Arr[i]==0 and check(i, Arr, length):
            # print(i)
            Arr[i]=1
            count += 1
    return count

if __name__ == "__main__":
    length = int(input())
    Arr = list(map(int, input().split()))
    count = insertNum(length, Arr)
    print(count)

## 测试用例：
# 输入：
# 10
# 0 0 1 0 0 0 0 1 0 0
# 输出：
# 3
