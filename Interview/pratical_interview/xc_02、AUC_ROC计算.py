## 计算AUC_ROC值

## 题目描述:ROC-AUC是一种常用的模型评价指标，它是ROC曲线下的面积。现在已知样本数据集的真实值(1为正样本，0为负样本)和某二分类器在该样本数据集上的预测值（属于正样本的概率，且各不相同），求ROC-AUC，精确到小数点后两位。

def AUC(xy_arr):
    auc = 0.			
    prev_x = 0
    for x,y in xy_arr:
        if x != prev_x:
            auc += (x - prev_x) * y
            prev_x = x
    return auc

if __name__ == "__main__":
    N = int(input())
    xy_arr = []
    for i in range(N):
        arr = list(map(float, input().split()))
        xy_arr.append(arr)
    auc = AUC(xy_arr)
    print(auc)

## 测试用例：
# 输入：
# 10
# 1 0.90
# 0 0.70
# 1 0.60
# 1 0.55
# 0 0.52
# 1 0.40
# 0 0.38
# 0 0.35
# 1 0.31
# 0 0.10
# 输出：
# 0。68