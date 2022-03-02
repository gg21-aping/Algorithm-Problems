# Typical Recursion Problem
# return a sequence of operations that transfer
# n rings from peg a to peg b

def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    # move top n-1 disks from origin to buffer, using destination as buffer
    TowerOfHanoi(n-1, source, auxiliary, destination)
    # move top from origin to destination
    print ("Move disk",n,"from source",source,"to destination",destination)
    # move top n-1 disks fro buffer to destination, using origin as a buffer
    TowerOfHanoi(n-1, auxiliary, destination, source)
         
# Driver code
n = 4
TowerOfHanoi(n,'A','B','C')
# A, C, B are the name of rods
