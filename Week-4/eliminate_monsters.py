class Solution:        
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        """
        sort with distance / speed with their time of arrival
        then eleminate starting from the first element
        Time: O(nlogn)
        space: O(n)
        """
        count = 0
        reachTime = [] # contains [time, distance, speed] of each element
        for index, dis in enumerate(dist):
            reachTime.append([math.ceil(dis/speed[index]), dis, speed[index]])
        reachTime.sort(key=lambda x: x[0])
        for j, elem in enumerate(reachTime):
            count += 1
            if j + 1 < len(reachTime):
                if reachTime[j + 1][1] -(count * reachTime[j + 1][2]) <= 0:
                    return count
        return count

# A more optimal solution 
# since you can kill a monster each minute
# class Solution(object):
#     def eliminateMaximum(self, dist, speed):
#         """
#         :type dist: List[int]
#         :type speed: List[int]
#         :rtype: int
#         """
#         time_reached = [dist / speed for dist, speed in zip(dist, speed)]
#         time_reached.sort()
#         num_killed = 0
#         for time in time_reached:
#             if time <= num_killed:
#                 return num_killed
#             num_killed += 1
#         return num_killed