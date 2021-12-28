class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        merge the duplicate intervals and return the non-overlappint intervals
        """
        myList = []
        max_int = float("-inf")
        min_int = float("+inf")
        for index in range(len(intervals) - 1, -1, -1):
            temp = index
            if intervals[index][1] > max_int:
                max_int = intervals[index][1]
            if  intervals[index][0] < min_int:
                min_int = intervals[index][0]
            while intervals[index][1] < intervals[index - 1][1] and temp > 0:
                intervals[index], intervals[index - 1]= intervals[index - 1], intervals[index]
                print(intervals)
        print(intervals)
        myList.append(intervals[0])
        # temp = 0
        
        for index in range(1, len(intervals)):
            for temp in range(len(myList)):
                if myList[temp][1] <= intervals[index][0]:
                    print(myList)
                    myList[temp][1] = intervals[index][1]
                    temp += 1
                elif myList[temp][1] > intervals[index][1] and myList[temp][1] > intervals[index][0] and myList[temp][0] > intervals[index][1]: 
                    continue
                else:
                    print(myList)
                    myList.append(intervals[index])
        for interval in myList:
            if  interval[0] < min_int and interval[1] > max_int:
                myList.remove(interval)
                # if len(myList) > 0 and myList[temp][1] <= intervals[index + 1]
                # else:
                #     temp += 1
                #     else:
                #         myList.append(intervals[i])
                #     pop = intervals.pop(temp + 1)
                #     print(index)
                #     # index -= 1
                #     # print(index)
                # # while intervals[i]
        print(myList)
        return myList
        