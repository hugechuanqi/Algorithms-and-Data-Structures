## 车辆时刻表分组
## 题目描述:某车站为了方便管理，决定根据目的地以及出发时间的不同对车辆时刻表进行分组管理。要求：给定一个时刻表，同一个目的地的车辆必须分配在同一组内，分组不能打乱时刻表的车次顺序，即各个分组之间出发时间有序。请对时刻表尽可能多的分组，按出发时间早晚作为输出顺序。

## 输入:时刻表内容：aabbcddc，a,b,c,d为目的地，字母出现的先后顺序为出发时间的先后顺序,例如aabbcddc
## 输出:输出各个分组的长度，以空格相隔，输出顺序与时刻表的出发顺序一致,例如,2,2,4

def getLength(strs):
    length_list = []
    res = []
    for elem in strs:
        if elem not in res:
            res.append(elem)
        else:
            if elem==res[0]:
                length_list.append(str(len(res)+1))
                res=[]
            else:
                res.append(elem)
    return length_list

if __name__ == "__main__":
    strs = input()
    res = getLength(strs)
    print(','.join(res))

## 测试用例：
# 输入：aabbcddc
# 输出：2,2,4s
