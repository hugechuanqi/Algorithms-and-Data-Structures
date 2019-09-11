class Solution(object):
    def maxSubArray(self, Arr):
        """ DP：最大子序和
        """
        tmp = Arr[0]
        max_ = tmp
        for i in range(1, len(Arr)):
            if tmp+Arr[i]>Arr[i]:
                max_ = max(max_, tmp+Arr[i])
                tmp = tmp + Arr[i]
            else:
                max_ = max(max_, tmp, tmp+Arr[i], Arr[i])
                tmp = Arr[i]
        return max_

if __name__ == "__main__":
    Arr = [-2,1,-3,4,-1,2,1,-5,4]
    a = Solution()
    maxSubSum = a.maxSubArray(Arr)
    print(maxSubSum)
