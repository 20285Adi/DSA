import sys

sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

#code here
def fibonacci(n):
    #base case
    if n == 1:
        return 0
    if n == 2:
        return 1
    #recurrence relation
    ans = fibonacci(n-2) + fibonacci(n-1)
    
    return ans
print(fibonacci(2))