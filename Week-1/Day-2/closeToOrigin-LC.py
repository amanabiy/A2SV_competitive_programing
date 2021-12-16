class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        should have used quick or merge sort
        Insertion sort have high time complexity
        so until learning quick and merge sort used built in wort
        """
        points.sort(key=lambda x: x[0]**2 + x[1]**2)
        # distance_index: List[tuple] = []
        # for index in range(len(points)):
        #     x: float = (points[index][0]) ** 2
        #     y: float = (points[index][1]) ** 2
        #     distance: float = sqrt(x + y) 
        #     position_distance = (distance, index)
        #     distance_index.append(position_distance)
        #     temp = len(distance_index) - 1
        #     while position_distance[0] < distance_index[temp - 1][0] and temp > 0:
        #         print(distance_index[temp])
        #         distance_index[temp], distance_index[temp - 1] = distance_index[temp - 1], distance_index[temp]
        #         temp -= 1
        # print(distance_index)
        # for point in range(len(points)):
        #     points[point] = points[distance_index[point][1]] 
        return points[:k]
            
    def calculateDistance(x1: int, y1: int) -> float:
        """ calculate the distance between points"""
        x = (x1) ** 2
        y= (y1) ** 2
        return sqrt(x + y)
