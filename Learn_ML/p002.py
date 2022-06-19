"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 
Notice that the solution set must not contain duplicate triplets.
"""

var1 = [-1,0,1,2,-1,-4]

output = []
sz = len(var1)
for i in range(sz):
    for j in range(i+1,sz):
        for k in range(j+1,sz):
            a,b,c = var1[i],var1[j],var1[k]
            if a!=b and a!=c and b!=c and a+b+c == 0:
                output.append([a,b,c])

for m in output:
    m.sort()
    output1.append(m)

print(output1)