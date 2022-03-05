class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        fWord = Counter(words)
        frequentWord = []
        ans = []
    
        for key, value in fWord.items():
            heapq.heappush(frequentWord, (-value, key))
        
        for i in range(k):
            ans.append(heapq.heappop(frequentWord)[1])

        return ans
        
