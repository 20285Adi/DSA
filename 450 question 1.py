import sys

sys.stdout = open('CP1/output.txt', 'w')
sys.stdin = open('CP1/input.txt', 'r')

#your code goes here
T = int(input())
for i in range(T):
    l = int(input())
    arr = list(map(int, input().split()))
    n = len(arr)
    arr_new = []
    for i in range(n):
        arr_new.append(arr[n-i-1])
    
    print(*arr_new)
    #print(arr_new)
