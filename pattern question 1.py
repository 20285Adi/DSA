import sys

sys.stdout = open('C:/Users/DEBASHISH THAKUR/Documents/CP/CP1/output.txt', 'w')
sys.stdin = open('C:/Users/DEBASHISH THAKUR/Documents/CP/CP1/input.txt', 'r')

#your code goes here
N = int(input())
for i in range(N):
    for j in range(N):
        print('*', end=" ")
    print()