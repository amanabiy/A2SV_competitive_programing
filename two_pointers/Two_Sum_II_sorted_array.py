class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Time: O(n)
        Space: O(1)
        """
        smaller = 0
        larger = len(numbers) - 1
        while larger > smaller:
            if numbers[smaller] + numbers[larger] == target:
                return [smaller + 1, larger + 1]
            if numbers[larger] + numbers[smaller] > target:
                larger -= 1
            else:
                smaller += 1