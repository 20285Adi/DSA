import sys

sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

#code here
##calculate sum of array using recursion
arr = [1,2,3,4,5,6,78,998,2]
# size = len(arr)
def sumarr(arr : int, size:int):
    ##base case
    if size == 0:
        return 0
    if size == 1:
        print(arr[0], end=" ")
        return arr[0]
    ##Recursive relation
    arr[1] = arr[1] + arr[0]
    sumarr(arr[1:], size-1)
    

sumarr([3,2,5,1,6], 5)



