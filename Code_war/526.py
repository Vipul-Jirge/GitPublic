def pf(LPFO:int = 100):
    i = 3
    #print(divFind)
    largest = LPFO**0.5
    while i < largest:
        if LPFO%i == 0 and LPFO != i:
            LPFO = LPFO//i
        i += 2
    return LPFO

def gn(n:int = 100):
    sum = 0
    for i in range(0,9+1):
        sum += pf(n+i)
        # print(sum)
    return sum

if __name__ == '__main__':
    print(gn())
    
    # import timeit

    # r = 1
    # print('old: ', timeit.repeat(lambda: pf(), number=r, repeat=3))
    # # print('new: ', timeit.repeat(lambda: pfnumpy(), number=r, repeat=3))
    # print(pf())