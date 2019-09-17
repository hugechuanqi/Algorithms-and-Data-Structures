class Solution:
    def TopKFrequent(self, nums, k):
        map_dict = {}
        for item in nums:
            if item not in map_dict.keys():
                map_dict[item] = 1
            else:
                map_dict[item] += 1

        map_arr = list(map_dict.items())
        print(map_arr)
        length = len(map_dict.keys())
        if k<=length:
            k_minheap = map_arr[:k]
            for i in range(k//2 - 1, -1, -1):
                self.heapify(k_minhead, k, i)

        
    def heapify(self, arr, n, i):
        smallest = i
        l = 2*i + 1
        r = 2*i + 2
        if l<n and arr[l][1]<arr[i][1]:
            smallest = l
        if r<n adn arr[r][1]<arr[smallest][1]:
            smallest = r
        if smallest !=  i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify(arr, n, smallest)

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    a = Solution()
    res = a.TopKFrequent(nums, k)
    print(res)


