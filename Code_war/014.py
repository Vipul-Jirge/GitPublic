'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet
(Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
ANS = 837799 in 
'''

@profile
def p14Old2(n:int = 1_000_000):
    storeVal = {1:1}
    midNumbr = []
    for numFlex in range (2,n):
        midNumbr = []
        while numFlex != 1 and numFlex not in storeVal:
            midNumbr.append(numFlex)
            if numFlex%2 == 0:
                numFlex = numFlex//2
            else:
                numFlex = 3*numFlex + 1
        if midNumbr != []:
            for i,m in enumerate(midNumbr[::-1]):
                storeVal[m] = i+1+storeVal[numFlex]

    # print([(i,storeVal[i]) for i in range(2,20)])
    return max(storeVal, key=storeVal.get)

def p14Old3(n:int = 1_000_000):
    storeVal = {}
    
    midNumbr = []
    for numbr in range (2,n):
        
        debug = []
        numFlex = numbr
        cns = 0
        if numFlex not in storeVal.keys():
            while numFlex != 1:
                debug.append(numFlex)
                if numFlex not in storeVal.keys():
                    if numFlex%2 == 0:
                        numFlex = numFlex//2
                    else:
                        numFlex = 3*numFlex + 1
                    cns +=1
                    # print(str(numFlex) + ': ' + str(cns) )
                    midNumbr.append(numFlex)
                else:
                    cns += storeVal[numFlex]
                    break
        # Store seq length in nos dict

        storeVal[numbr] = cns
        for i in range(1,cns+1):
            storeVal[midNumbr[i-1]] = cns-i
        # print(storeVal)
        # print(debug)
    return max(storeVal, key=storeVal.get)
	


if __name__ == '__main__':
    print(p14Old2())
    # print(p14Old3(20))