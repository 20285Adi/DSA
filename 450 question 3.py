import sys

sys.stdout = open('CP1/output.txt', 'w')
sys.stdin = open('CP1/input.txt', 'r')

#your code goes here
class Solution:
    def sort012(self,arr,n):
        # code here
        low = 0
        mid = 0
        high = n - 1
        for i in arr:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                mid += 1
                low += 1
            elif arr[mid] == 2:
                arr[mid], arr[high] = arr[high], arr[mid]
                #mid += 1
                high -= 1
        return arr