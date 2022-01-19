'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

def run(n:int):
    a:int = 2**n
    numstr:str = str(a)
    sumstr = 0
    for i in range(len(numstr)):
        sumstr += int(numstr[i])
    return sumstr


if __name__ == "__main__":
    print(run(1000))