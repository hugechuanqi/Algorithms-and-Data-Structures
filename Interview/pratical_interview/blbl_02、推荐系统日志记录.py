def getMostTouch(N, Arr):
    countSet ={}
    maxNum = 0
    for i in range(N):
        fro = Arr[i][0] 
        to = Arr[i][1]
        if to not in countSet.keys():
            countSet[to] = fro
        elif fro>countSet[to]:
            countSet[to] = fro
        if to>maxNum:
            maxNum = to
    return countSet[maxNum]

if __name__ == "__main__":
    N = int(input())
    Arr = []
    for i in range(N):
        temp = list(map(int, input().split()))
        Arr.append(temp)
    res = getMostTouch(N,Arr)
    print(res)

## 测试用例：
# 输入：
# 5
# 33956 27538
# 79731 91415
# 25288 33956
# 33956 84925
# 79731 25288
# 输出：
#79731



def getMostTouch(Arr):
    countSet ={}
    maxNum = 0
    for elem in set(Arr):
        num = Arr.count(i)
        countSet[num]=elem
        if num>maxNum:
            maxNum = num
    return countSet[maxNum]

if __name__ == "__main__":
    N = int(input())
    Arr = []
    for i in range(N):
        temp = list(map(int, input().split()))
        Arr.append(temp[0])
    res = getMostTouch(Arr)
    print(res)