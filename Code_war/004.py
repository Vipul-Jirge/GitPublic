"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
ans = 906609 in 0.0189228 s
"""

def run():
    allKs = ([])
    for i in range (999,900,-1):
        for j in range (999,900,-1):
            k = i*j
            Sk = str(k)
            if Sk == Sk[::-1]:
                allKs.append(k)
    LargePal = max(allKs)
    return LargePal

if __name__ == '__main__':
    print(run())