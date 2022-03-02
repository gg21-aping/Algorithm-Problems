# sort a stack such that the smallest element are on the top.
# using mutiple stacks is acceptable, 
# but copying element to other data structure is not.
# similar to pancake problem where you flip the stack again and again

def sortStack(stack):
    
    buffer = []

    while stack:
        # insert each element in stack in order into buffer
        temp = stack.pop()
        while buffer and buffer[-1] > temp:
            stack.append(buffer.pop())
        buffer.append(temp)
    
    # copy the element from buffer back to stack
    # flip the entire buffer so that 
    # the smallest element is at the top of the stack
    while buffer:
        stack.append(buffer.pop())

# time complexity O(n^2), space complexity O(n)
# test case
stack = [1,3,8,12,5,10,7]
sortStack(stack)
print(stack)

