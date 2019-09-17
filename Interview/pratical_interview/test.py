
def buyMinNum(N, Arr):
    nums = [1]*N
    for i in range(N-1):
        if Arr[i+1]>Arr[i]:
            nums[i+1] = nums[i] + 1
    # print(nums)
    for j in range(N-1, 0, -1):
        if Arr[j-1]>Arr[j] and nums[j-1]<=nums[j]:
            nums[j-1] = nums[j] + 1
    # print(nums)
    return sum(nums)

if __name__ == "__main__":
    N = 6
    Arr = [3,6,3,5,6,2]
    num = buyMinNum(N, Arr)
    print(num)


