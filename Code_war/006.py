'''
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
ans = 25164150 in 6.49562e-06
'''

def run(n:int= 100):
    j = 0
    k = 0
    for i in range(1,n+1):
        j = j+i**2
        k += i/2
    return k**2 - j

def runN(n:int= 100):
    j = 0
    k = (0.5*n*(n+1))**2
    for i in range(1,n+1):
        j = j+i**2
    return k - j

if __name__ == '__main__':
    print(run(100))
    print(runN(100))
    import timeit
    r = 100_000
    print('old: ', timeit.repeat(lambda: run(10), number=r, repeat=1))
    print('new: ', timeit.repeat(lambda: runN(1_0), number=r, repeat=1))