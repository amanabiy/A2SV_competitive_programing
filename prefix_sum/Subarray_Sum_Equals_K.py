class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total_sum = 0
        seen = defaultdict(int)
        count = 0
        seen[0] = 1
        for num in nums:
            total_sum += num
            count += seen[total_sum - k]
            seen[total_sum] += 1
        return count
                
