import sys

sys.stdout = open('C:/Users/DEBASHISH THAKUR/Documents/CP/CP1/output.txt', 'w')
sys.stdin = open('C:/Users/DEBASHISH THAKUR/Documents/CP/CP1/input.txt', 'r')

#your code goes here
#lcm
x = int(input())
y = int(input())
higher = max(x,y)
value = higher
while(True):
    if higher % x == 0 and higher % y == 0:
        lcm = higher
        print(f'lcm is {lcm}')
        break
    else:
        higher = higher + value

#gcd
gcd = int(x*y/lcm)
print(gcd)