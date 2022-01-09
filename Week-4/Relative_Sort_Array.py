class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        sort relative to given array Time: O(nlogn) Space: O(m)
        where n: size of arr1
        and m: size of arr2
        """
        count = defaultdict(int)
        for index, num in enumerate(arr2):
            count[num] = index
        arr1.sort(key=lambda x: [count[x]] if x in count else [float('inf'), x])
        return arr1