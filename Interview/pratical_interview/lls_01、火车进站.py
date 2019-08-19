## 题目：火车进站
## 类型：动态规划，字典排序

## 思路：首先由于火车到站时间不一定排序，因此首先需要将火车的进站时间和出站时间构建成字典，然后对字典进行排序，最后以火车的出站时间为最小值，求比其小的进站时间，每当进站时间<出站时间时，就必须得多添加一次站台，加上本次火车的站台，则为火车战最小的站台数量。

class train:
    def __init__(self, train_in, train_out):
        self.train_in_ = train_in
        self.train_out_ = train_out

def getMinTrain(train):
    res = [0]*len(train)
    for i in range(len(train)-1):   #以出站时间为索引
        count = 1
        for j in range(i+1, len(train)):    # 以如栈时间为索引
            if train[i][1]>train[j][0]:
                count += 1
        res[i] = count
    print(res)
    return max(res)

import operator
if __name__ == "__main__":
    # train_in = list(map(int, input().split()))
    # train_out = list(map(int, input().split()))
    train_in = [900, 940, 950, 1100]
    train_out = [910, 1200, 1120, 1130]
    time_dict = {}
    for i in range(len(train_in)):
        time_dict[train_in[i]] = train_out[i]
    print(time_dict)
    train_time = sorted(time_dict.items(),key = operator.itemgetter(0))   #对字典进行排序，0表示以key进行排序，1表示以value进行排序
    print(train_time)
    num = getMinTrain(train_time)
    print(num)
