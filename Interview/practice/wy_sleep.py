## 瞌睡：
# 只能叫醒他一次，总分数=醒着的分数+睡着被叫醒的额外的分数

n, k = list(map(int, input().split()))
scores = list(map(int, input().split()))
awakes = list(map(int, input().split()))

# 醒着的状态的分数
awake_score = 0
for i in range(n):
    if awakes[i]:
        awake_score += scores[i]
        scores[i] = 0

# 睡着被叫醒的状态获得的分数
inawake_score = 0
for i in range(n):
    if not awakes[i]:
        boost_score = sum(scores[i:min(i+k, n)])
        inawake_score = max(inawake_score, boost_score)

print(awake_score+inawake_score)

#测试用例
# 输入：
# 6 3
# 1 3 5 2 5 4
# 1 1 0 1 0 0
# 输出：
#16