class KthLargest:
    
    def heapify(self, arr, n, i):
        larger = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n:
            larger = l if arr[l] < arr[larger] else larger
        if r < n:
            larger = r if arr[r] < arr[larger] else larger
        if larger != i:
            arr[larger], arr[i] = arr[i], arr[larger]
            self.heapify(arr, n, larger)

            
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        i = len(nums) // 2
        while i >= 0:
            self.heapify(self.nums, len(nums), i)
            i -= 1
        if k < len(nums):
            self.nums[:] = self.nums[len(nums) - k:] 
            i = len(self.nums) // 2
            while i >= 0:
                self.heapify(self.nums, len(self.nums), i)
                i -= 1
        

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            self.nums.append(val)
            self.heapify(self.nums, len(self.nums), 0)
            return self.nums[0]
        if self.nums[0] > val:
            return self.nums[0]
        self.nums[0] = val
        self.heapify(self.nums, len(self.nums), 0)
        return self.nums[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
