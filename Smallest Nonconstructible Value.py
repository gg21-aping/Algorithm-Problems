# time complexity O(nlogn): sort (nlogn) and iterate (n)

def smallest(array):
    max_value = 0
    for num in sorted(array):
        if num > max_value + 1: break
        max_value += num
    return max_value + 1

# test case
array = [12,2,1,15,2,4]
print(smallest(array))