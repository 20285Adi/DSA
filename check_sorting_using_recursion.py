import sys

sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

#code here
##check if array is dorted or not using recursion
#return true if sorted, return false if not
arr = [1,2,3,4,5,6,78,998,2]
size = len(arr)
def sortedarr(arr, size):
    ##base case
    if (size == 0 or size == 1):
        print('True', end="")
        return True
    ##calculation
    if arr[0] > arr[1]:
        print('False', end = "")
        return False
    else:
        ##Recursive Relation
        ans = sortedarr(arr[1:] , size-1)
        return ans

sortedarr(arr, size)


