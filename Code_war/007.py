"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
ans = 104743
"""
import math

def run(n:int = 10_001):
    till = math.ceil(n*math.log(n)+n*math.log(math.log(n)))
    allNos = [x for x in range(3,till+1,2)]
    # print(allNos)
    cns = 0
    for div in allNos: #o(n)
        cns += 1
        if div+cns >= (n**0.5):
            continue
        allNos = [num for num in allNos if num%div != 0 and num != div]
    allNos.append(2)
    allNos.append(3)
    allNos.sort()

    return allNos


def runO(n:int = 10_001):
    Prime = []
    isPrime = 1
    while len(Prime) < 10_001:
        isPrime += 1
        for i in Prime:
            if isPrime%i == 0:
                #print(isPrime,'isnt Prime')
                break
        else:
            Prime.append(isPrime)

    return Prime[-1]

if __name__ == '__main__':
    print(run())
    import timeit

    # r = 1
    # print('old: ', timeit.repeat(lambda: run(), number=r, repeat=3))