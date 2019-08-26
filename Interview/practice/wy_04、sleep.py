## 题目：瞌睡
## 类型：数组，贪心

## 题目描述：小易觉得高数课太无聊了，决定睡觉。不过他对课上的一些内容挺感兴趣，所以希望你在老师讲到有趣的部分的时候叫醒他一下。你知道了小易对一堂课每分钟知识点的感兴趣程度，并以分数量化，以及他在这堂课上每分钟是否会睡着，你可以叫醒他一次，这会使得他在接下来的k分钟内保持清醒。你需要选择一种方案最大化小易这堂课听到的知识点分值。

## 核心：
## 思路： 只能叫醒他一次，总分数=醒着的分数+睡着被叫醒的额外的分数

def getScore(n, k, scores, awakes):
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
        score = awake_score+inawake_score
        return score

if __name__ == "__main__":
        n, k = list(map(int, input().split()))
        scores = list(map(int, input().split()))
        awakes = list(map(int, input().split()))
        score = getScore(n, k, scores, awakes)
        print(score)

#测试用例
# 输入：
# 6 3
# 1 3 5 2 5 4
# 1 1 0 1 0 0
# 输出：
#16