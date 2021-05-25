# Fibonacci sum in python using recursion

def calFibonacci(num):
    if num in [0,1]:
        return num
    else:
        return calFibonacci(num-1)+calFibonacci(num-2)

print(calFibonacci(6))