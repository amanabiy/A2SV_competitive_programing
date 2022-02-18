class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        n = 0
        i = 0
        while len(nums) > i:
            if nums[i] == 0:
                n += 1
            else:
                if n != zero:
                    nums[n], nums[zero] = nums[zero], nums[n]
                n+= 1
                zero+=1
            i+=1
