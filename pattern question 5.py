import sys

sys.stdout = open('C:/Users/DEBASHISH THAKUR/Documents/CP/CP1/output.txt', 'w')
sys.stdin = open('C:/Users/DEBASHISH THAKUR/Documents/CP/CP1/input.txt', 'r')

#your code goes here
N = int(input())
#loop lagao for number of rows
for i in range(N):
    for j in range(i, N):
        print('*', end=" ")
    print()
