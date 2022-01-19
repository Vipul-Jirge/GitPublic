'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
ans = 232792560
'''

def runN(n:int = 2_0):
    allNos = [x for x in range(3,n+1,2)]
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

    multlist = [i for i in range(1,n+1)] # [1,2,3,4,5,6,7,8,9,10]
    i = 2
    while i < len(multlist):
        if i not in allNos:
            for j in range(0,i):
                if multlist[i]%multlist[j] == 0:
                    multlist[i] = multlist[i]//multlist[j]
        i+=1

    j = 1
    for i in multlist:
        j*=i

    return j,multlist

def run(n:int = 2_0):
    multlist = [i for i in range(1,n+1)] # [1,2,3,4,5,6,7,8,9,10]
    i = 2
    while i < len(multlist):
        for j in range(0,i):
            if multlist[i]%multlist[j] == 0:
                multlist[i] = multlist[i]//multlist[j]
        i+=1

    j = 1
    for i in multlist:
        j*=i

    return j,multlist


if __name__ == '__main__':
    import timeit

    r = 1
    print('old: ', timeit.repeat(lambda: run(2_0), number=r, repeat=1)) 
    print('new: ', timeit.repeat(lambda: runN(2_0), number=r, repeat=1))