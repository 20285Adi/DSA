import sys

sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

#code here
##fibonacci using for loop
n = int(input())
a = 0
b = 1
for i in range(2, n+1):
    c = a + b
    a, b = b, a+b
print(c, end = "")