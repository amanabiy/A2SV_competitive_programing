#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        selected = i
        for index in range(i, len(arr)):
            if arr[index] < arr[selected]:
                selected = index
        return selected
    
    def selectionSort(self, arr,n):
        #code here
        for index in range(n):
            sort = self.select(arr, index)
            if sort != index:
                arr[index], arr[sort] = arr[sort], arr[index]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends