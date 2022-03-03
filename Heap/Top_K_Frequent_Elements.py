class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time: O(Klogn + n)
        Space: O(n)
        """
        value_freq = Counter(nums)
        ans = []

        for key, value in value_freq.items():
            if not ans or len(ans) < k:
                heapq.heappush(ans, (value, key))
            elif ans[0][0] < value:
                heapq.heappop(ans)
                heapq.heappush(ans, (value, key))
                
        return [ a[1] for a in ans ]
        
        # with heap and still Time: O(nlogn) Space: O(n)
        # value_freq = Counter(nums)
        # ans = []
        # answer = []
        # heapq.heapify(ans)
        # for key, value in value_freq.items():
        #     heapq.heappush(ans, (-value, key))
        #     # print( value_freq[ans[0]], value,  value_freq[ans[0]] < value)
        # for i in range(k):
        #     answer.append(heapq.heappop(ans)[1])
        # return [ a[1] for a in answer]


        # with dictionary and sort Time: O(nlogn) space: O(n)
        # print( sorted(value_freq.items(), key=lambda i: i[1]))
        # for key, value in sorted(value_freq.items(), key=lambda i: i[1], reverse=True):
        #     if not ans or len(ans) < k:
        #         ans.append(key)
        # return ans
