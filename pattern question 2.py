import sys

sys.stdout = open('C:/Users/ADITI DAS/Documents/CP/CP1/output.txt', 'w')
sys.stdin = open('C:/Users/ADITI DAS/Documents/CP/CP1/input.txt', 'r')

#your code goes here
N = int(input())
#first number of rows ke liye loop lagao
for i in range(N):
    #har loop mei increase the range of j by one
    for j in range(0, i+1):
        print('* ', end=" ")
    print()
       
    
