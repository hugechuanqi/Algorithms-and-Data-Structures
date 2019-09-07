# 检测是否为回文序列
class Solution:
    def shrinkCheckPalindrome(self, Arr, low, high):
            while(low<=high):
                if Arr[low] == Arr[high]:
                    low += 1
                    high -= 1
                else:
                    return False
            return True

if __name__ == "__main__":
    Arr = list(map(int, input().split()))
    a = Solution()
    print(a.shrinkCheckPalindrome(Arr, 0, len(Arr)-1))

