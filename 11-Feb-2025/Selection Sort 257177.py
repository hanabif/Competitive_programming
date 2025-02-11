# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        n=len(arr)
        
        for i in range(n):
            minIndex=i
            for j in range(i+1,n):
                if arr[minIndex]>arr[j]:
                    minIndex=j
            arr[i],arr[minIndex]=arr[minIndex],arr[i]
        return arr