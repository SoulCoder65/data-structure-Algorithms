# Python program to find factorial using recurrison



def calFact(num):
    assert num>0 and int(num)==num,"Number must be positive integer"
    if num in [0,1]:
        return 1
    else:
        return num*calFact(num-1)


print(calFact(3))