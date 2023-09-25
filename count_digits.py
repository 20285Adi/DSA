import sys



sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

#code here
count = 0
N = int(input())
my_list = [int(i) for i in str(N)]
# print(my_list)
for j in my_list:
    if j > 0 and N % j == 0:
        count += 1
print(count)
    