
def minimumAverage(customers):
    # Write your code here
    n = len(customers)
    customers.sort(reverse=True)
    currentTime = customers[-1][0]
    totalServeTime = 0
    heap = []
    while heap or customers:
        if not heap:
            enterTime, cookTime = customers.pop()
            currentTime = max(currentTime, enterTime)
            heapq.heappush(heap, (cookTime, enterTime))
        else:
            serveTime, inTime = heapq.heappop(heap)
            totalServeTime += max(currentTime - inTime, 0) + serveTime
            currentTime += serveTime
            while customers and (customers[-1][0] <= currentTime):
                val = customers.pop()
                heapq.heappush(heap, (val[1], val[0]))
            # print(totalServeTime, currentTime - enterTime, currentTime)
    return  totalServeTime // n
