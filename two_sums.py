#brute force approach
target = int(input())
arr = list(map(int, input().split()))
hashmap = {}
for i, n in enumerate(arr):
    diff = target - n
    if diff in hashmap:
        print([hashmap[diff], i])
    else:
        hashmap[n] = i
       