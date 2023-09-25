import sys

sys.stdout = open('CP1/output.txt', 'w')
sys.stdin = open('CP1/input.txt', 'r')

#your code goes here
n = int(input())
arr = list(map(int, input().split()))
p_lst = []
n_lst = []
for i in arr:
    if i >= 0:
        p_lst.append(i)
    elif i < 0:
        n_lst.append(i)
print(*p_lst + n_lst)
