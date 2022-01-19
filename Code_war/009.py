"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
ANS = 31875000 in 0.00625 x 20 (200, 375, 425)

"""

# import math

def runO(n:int =1000):
    for a in range(1,n//2):
        for b in range(a+1,n//2):
            if (n-a-b)**2 == (b**2 + a**2): # pyth triplet
                return a*b*(n-a-b)

def run(n:int = 1000):
    for a in range(1,n//2):
        b:int = (2*a*n - n**2)//(2*a - 2*n)
        if (n-a-b)**2 == (b**2 + a**2): # pyth triplet
                return a*b*(n-a-b)

if __name__ == '__main__':
    print(runO())
    print(run())
    import timeit

    r = 20
    print('old: ', timeit.repeat(lambda: runO(), number=r, repeat=1))
    print('new: ', timeit.repeat(lambda: run(), number=r, repeat=1))
    # print(pythNew())