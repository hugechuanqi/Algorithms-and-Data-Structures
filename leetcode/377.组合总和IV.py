class Solution:
    def combinationSum4(self, nums, target):
        
        # f(4) = (f(3) ) + (f(2) ) + (f(1) ) 
        
        dp = [0] * (target + 1)
        
        for n in nums:
            if (n <= target):   # 
                dp[n] += 1
        
        for i in range(1,target+1):
            
            for n in nums:
                if(i >= n):
                    dp[i] += (dp[i - n])
        print(dp)
        return dp[target]

    def combinationSum42(self, nums, target):
        size = len(nums)
        if size == 0 or target <= 0:
            return 0

        dp = [0 for _ in range(target + 1)]
        
        # 这一步很关键，想想为什么 dp[0] 是 1
        # 因为 0 表示空集，空集和它"前面"的元素凑成一种解法，所以是 1
        # 这一步要加深体会
        
        dp[0] = 1

        for i in range(1, target + 1):      # 每个i代表1～target之间的目标值
            for j in range(size):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]
        print(dp)
        return dp[-1]

if __name__ == "__main__":
    target = 10
    nums = [2,3,5]
    a = Solution()
    res = a.combinationSum42(nums, target)
    print(res)
