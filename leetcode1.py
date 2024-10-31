"""
Given an integer array num, return an array such that ans[i] is equal to product
of all elements of num except num[i]
"""

num = [int(x) for x in input().split()]
ans = []

for i in range(len(num)):
    subList = num[:i] + num[i+1:]
    prod = 1
    for elem in subList:
        prod *= elem
    ans.append(prod)

print(ans)
