# find the min and max simultaneously in an array
import collections
def findMinMax(array):
    MinMax = collections.namedtuple('MinMax', ("small", "big"))
        
    def min_max(a, b):
        return MinMax(a, b) if a < b else MinMax(b, a)
        
    # base case
    if len(array) == 1:
        return []
    
    current = min_max(array[0], array[1])
    # process comparation between two numbers a time
    for i in range(2, len(array) - 1, 2):
        temp = min_max(array[i], array[i + 1])
        current = MinMax(
            min(current.small, temp.small), 
            max(current.big, temp.big)
        )
    # if there is odd numbers in the array: 
    if len(array) & 1:
        current = MinMax(
            min(current.small, array[-1]),
            max(current.big, array[-1])
        )

    return current

# test case
A = [3,2,5,1,2,4]
answer = findMinMax(A)
print(answer)