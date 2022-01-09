class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """ Time: O(nlogn) Space: O(n)"""
        minute = [(int(time.split(":")[0]) * 60 + int(time.split(":")[1])) for time in timePoints]
        minute.sort()
        answer = min(minute[-1] - minute[0], 1440 - minute[-1] + minute[0])
        for i in range(len(timePoints)-1):
            answer = min(answer, minute[i + 1] - minute[i],
                         1440 + minute[i] - minute[i + 1])
        return answer