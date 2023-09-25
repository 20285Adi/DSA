import sys

sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

#code here
##say digit
arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
def saydigit(n):
    ##base case
    if n == 0:
        return
    #calculation
    digit = n % 10
    n = n//10
    ##Recursive Relation
    saydigit(n)
    #print function
    print(arr[digit])
saydigit(1234567890)
