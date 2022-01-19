
# ans  = 233168 in 0.0009432 s


def runO(n:int = 1000):
    a = 0
    for i in range(n):
        if i%5 == 0 or i%3 == 0:
            a+=i
            # print(i)
    return a

def run(n:int = 1000):
    three = 3*(n//3*(n//3+1))//2
    five = 5*(n//5*(n//5+1))//2
    fifteen = 15*(n//15*(n//15+1))//2

    return three+five-fifteen

if __name__ == '__main__':
    print(run())
    print(runO())
    
    import timeit
    r = 1000
    print('old: ', timeit.repeat(lambda: runO(), number=r, repeat=1))
    print('new: ', timeit.repeat(lambda: run(), number=r, repeat=1))