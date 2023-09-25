import sys

sys.stdout = open('C:/Users/DEBASHISH THAKUR/Documents/CP/CP1/output.txt', 'w')
sys.stdin = open('C:/Users/DEBASHISH THAKUR/Documents/CP/CP1/input.txt', 'r')

#your code goes here
N = input()
sum = 0
power = len(N)
for i in N:
    sum += int(i)**power
if sum == int(N):
    print("Yes")
else:
    print("No")
