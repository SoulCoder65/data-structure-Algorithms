# python program to find sum of digit of number using recurrsion

def calSumOfDigits(num):
    if num==0:
        return num
    else:
        return int(num%10)+calSumOfDigits(int(num/10))

print(calSumOfDigits(12345678910))
