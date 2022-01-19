"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

def run():
    num = 1
    den = 1
    for i in range(10, 100):
        iten = i//10
        iunit = i-iten*10
        for j in range(i+1,100):
            jten = j//10
            junit = j-jten*10
            k = i/j
            if (iten==jten or iten==junit or iunit==jten or iunit==junit):
                if iunit!=0 and junit != 0:
                    if iten==jten:
                        a = iunit/junit
                    if iten==junit:
                        a = iunit/jten
                        # print(min(iunit,jten),max(iunit,jten))
                    if iunit==jten:
                        a = iten/junit
                    if iunit==junit:
                        a = iten/jten
                    # print(i,'/',j, '=', k,'a=',a)
                    if k == a:
                        # print(j/i)
                        num *= i
                        den *= j
                        # print(i,'/',j, '=', k)#,' ,a=', a)
    denval = den/num
    return denval

def runO():
    singles = []
    for i in range(1,10):
        for j in range(i+1,10):
            k = i/j
            if k not in singles:
                singles.append(k)
    # print(singles)
    # singles = [i for i in range(1,10)]
    # all multiples of 10 are eliminated: 0/2 = 0
    num = 1
    den = 1
    for i in range(10, 100):
        iten = i//10
        iunit = i-iten*10
        for j in range(i+1,100):
            jten = j//10
            junit = j-jten*10
            k = i/j
            if (iten==jten or iten==junit or iunit==jten or iunit==junit):
                if (k in singles):
                    if iunit!=0 and junit != 0:
                        if iten==jten:
                            a = iunit/junit
                        if iten==junit:
                            a = iunit/jten
                            # print(min(iunit,jten),max(iunit,jten))
                        if iunit==jten:
                            a = iten/junit
                        if iunit==junit:
                            a = iten/jten
                        # print(i,'/',j, '=', k,'a=',a)
                        if k == a:
                            # print(j/i)
                            num *= i
                            den *= j
                            # print(i,'/',j, '=', k)#,' ,a=', a)
    denval = den/num
    return denval

if __name__ == '__main__':
    # print(run())
    # print(runO())
    
    import timeit
    r = 1000
    print('old: ', timeit.repeat(lambda: runO(), number=r, repeat=1))
    print('new: ', timeit.repeat(lambda: run(), number=r, repeat=1))