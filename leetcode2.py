"""
given an integer arr, move all zeros to the end of it while maintaining the order
of the remaining elems
"""

arr = [int(x) for x in input().split()]

for elem in arr:
    if elem == 0:
        arr.remove(elem)
        arr.append(elem)

print(arr)
