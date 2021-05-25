# python program to find power of number using recurssion

def calPower(num,powr):
    if powr==0:
        return 1
    if powr==1:
        return num
    else:
        return num*calPower(num,powr-1)

print(calPower(12,100))
