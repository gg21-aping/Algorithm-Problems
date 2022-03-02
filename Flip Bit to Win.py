# You have an integer and you can flip exactly one bit from a 0 to a 1.
# find the length of the longest subsequence of 1s you could create
# input: 1775 (11011101111)
# output: 8

from ctypes import sizeof

# time complexity O(b), where b is the number of bits
# space complexity O(1)
def flipBit(num):
    # if all bits are 1s
    if ~num == 0: return 8 * sizeof()

    currLen, prevLen, maxLen = 0, 0, 0

    while num > 0:
        # if current bit is 1, increment current length
        if num & 1: currLen += 1
        # uf current bit is 0, check next bit of num
        else: # not num & 1
            # update previous length to 0 (if next bit is 0)
            # or to currLen if next bit is 1
            prevLen = 0 if num & 2 == 0 else currLen
            currLen = 0
        # update maxLen if required
        maxLen = max(maxLen, currLen + prevLen)
        # right shift num
        num >>= 1
    
    return maxLen + 1

# test case
# input 1
print(flipBit(13))
 
# input 2
print(flipBit(1775))
 
# input 3
print(flipBit(15))
