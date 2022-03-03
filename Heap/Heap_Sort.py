#User function Template for python3

class Solution:
    def leftChild(self, index):
        return index * 2 + 1

    def rightChild(self, index):
        return index * 2 + 2

    def parent(self, index):
        return (index - 1) // 2

    def insert(self, arr, n, val):
        # insert a new element at the end
        arr.append(val)
        self.heapify(arr, n + 1, len(arr) - 1)

    def remove(self, arr, n):
        self.swap(arr, 0, len(arr))
        arr.pop()
        self.heapify(arr, n - 1, 0)
        
    def modifiy(self, arr, i, val):
        temp = arr[i]
        arr[i] = val
        if temp < val:
            self.heapifyUp(arr, n, i)
        if temp > val:
            self.heapify(arr, n, i)
            

    def swap(self, arr, index1, index2):
        arr[index1], arr[index2] = arr[index2], arr[index1]
    
    # heapify up
    def heapifyUp(self, arr, n, i):
        p = self.parent(i)
        if p >= 0:
            if arr[i] > arr[p]:
                self.swap(arr, p, i)
                self.heapifyUP(arr, n, p)
        
        
    
    #Heapify function to maintain heap property.
    # heapify down
    def heapify(self,arr, n, i):
        # code here
        # heapify down if the parent is larger and then 
        l = self.leftChild(i)
        r = self.rightChild(i)
        larger = i
        if l < n:
            larger = l if arr[l] > arr[larger] else larger
        if r < n:
            larger = r if arr[r] > arr[larger] else larger
        if larger != i:
            # print("moving", larger, i)
            self.swap(arr, larger, i)
            self.heapify(arr, n, larger)
            

    #Function to build a Heap from array.
    def buildHeap(self,arr,n):  
        # code here
        i = n - 1
        while i >= 0:
            # print(arr, arr[i])
            self.heapify(arr, n, i)
            i -= 1
        print(arr)
        # print(arr)
        # print('-------------------')
            
        
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr, n)
        for i in range(len(arr) -1, 0, -1):
            self.swap(arr, 0, i)
            # print(arr)
            self.heapify(arr, i, 0)

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends
