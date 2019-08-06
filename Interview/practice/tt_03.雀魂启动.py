## 题目：雀魂启动
## 类型：数组类问题
## 要求：
    # 总共有36张牌，每张牌是1~9。每个数字4张牌。
    # 你手里有其中的14张牌，如果这14张牌满足如下条件，即算作和牌

    # 14张牌中有2张相同数字的牌，称为雀头。
    # 除去上述2张牌，剩下12张牌可以组成4个顺子或刻子。顺子的意思是递增的连续3个数字牌（例如234,567等），刻子的意思是相同数字的3个数字牌（例如111,777）


## 输入：输入只有一行，包含13个数字，用空格分隔，每个数字在1~9之间，数据保证同种数字最多出现4次。
## 输出：输出同样是一行，包含1个或以上的数字。代表他再取到哪些牌可以和牌。若满足条件的有多种牌，请按从小到大的顺序输出。若没有满足条件的牌，请输出一个数字0
## 例如：输入：1 1 1 2 2 2 5 5 5 6 6 6 9            输出：9

## - 思路：将所有可能出现的牌加入到手牌中，然后递归判断是否满足雀头、顺子或刻子的条件。

class Solution():
    def isHu(self, nums):
        if not nums:
                return True
        n = len(nums)
        count0 = nums.count(nums[0])
        # 没出现过雀头，且第一个数字出现的次数 >= 2,去掉雀头剩下的能不能和牌
        if n % 3 != 0 and count0 == 2 and self.isHu(nums[2:]) == True:
            return True
        # 如果第一个数字出现次数 >= 3，去掉这个刻子后看剩下的能和牌
        if count0 == 3 and self.isHu(nums[3:]) == True:
            return True
        # 如果存在顺子，移除顺子后剩下的能和牌
        if nums[0] + 1 in nums and nums[0] + 2 in nums:
            last_nums = nums.copy()
            last_nums.remove(nums[0])
            last_nums.remove(nums[0] + 1)
            last_nums.remove(nums[0] + 2)
            if self.isHu(last_nums) == True:
                return True
        # 以上条件都不满足，则不能和牌
        return False

    def add_card_main(self, array):
        number_dict = {}
        for elem in array:
            number_dict[elem] = number_dict.get(elem, 0) + 1

        card_list = set(range(1,10)) - {elem for elem,number in number_dict.items() if number ==4}
        res = []
        for i in card_list:
            if self.isHu(sorted(array + [i])):
                res.append(i)
        return res

a = Solution()
array = list(map(int, input().split()))
res = a.add_card_main(array)
res = ' '.join(str(x) for x in sorted(res)) if res else '0'
print(res)

## 测试用例：
# 输入：
# 1 1 1 3 4 5 5 5 5 6 7 9 9
# 输出：
# 2 8 9
