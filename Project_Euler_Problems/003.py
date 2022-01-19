
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

improvise: 71*1471*839*6857 change i // value cumulitively

Current code: for nos containing prime numbers upto 7 digits
ans = 6857 in 0.071 s
"""
# import numpy as np

# @profile
def pf(LPFO:int = 600851475143):
    previsprime = 0
    i = 3
    c = []
    j = []
    #j.append(2)
    isprime = 0
    divFind = 10
    while LPFO//divFind > 10000000:
        divFind = divFind*10

    #print(divFind)
    div  = divFind
    while i < LPFO//div:
        # a = LPFO%i
        if LPFO%i == 0:
            j.append(i)
            for k in j:
                if i%k == 0:
                    isprime = k
                    break
            c = max(isprime,previsprime)
            previsprime = c
        i += 2

        # print(i)
    return c

# @profile
def pfnumpy(LPFO:int = 600851475143):
    i = 3
    #print(divFind)
    largest = LPFO**0.5
    while i < largest:
        if LPFO%i == 0 and LPFO != i:
            LPFO = LPFO//i
        i += 2

        # print(i)
    return LPFO


if __name__ == '__main__':
    # print(pf())
    
    import timeit

    r = 1
    print('old: ', timeit.repeat(lambda: pf(), number=r, repeat=3))
    print('new: ', timeit.repeat(lambda: pfnumpy(), number=r, repeat=3))
    print(pfnumpy())