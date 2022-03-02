# Determine the number of bits you would need to flip
# to convert integer A to integer B
# input: 29 (11101), 15 (01111)
# output: 2

# Each 1 in XOR represents a bit that is different between A and B
def bitSwapRequired(a, b):
    count = 0
    c = a ^ b
    while c:
        if c & 1: count += 1
        c = c >> 1
    return count

# Optimization 
# c = c & (c - 1) clear the right-most (least significant) bit
def optimizedBitSwap(a, b):
    count = 0
    c = a ^ b
    while c:
        count += 1
        c &= c - 1
    return count

# test case 
print(bitSwapRequired(29, 15))
print(optimizedBitSwap(29, 15))