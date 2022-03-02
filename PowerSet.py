class Solution:
    def recursion(self, nums):
        # time complexity O(n2^n)
        # compute all subsets U that do not include a particular element
        # compute all subsets V that include the element
        # final result is just U || V
        def powerSet(toSelect, selected):
            # base case: input set is empty, return {{}}
            if toSelect == len(nums):
                powerset.append(list(selected))
                return 
            
            powerSet(toSelect + 1, selected)
            # generate all subsets that contain nums[toSelect]
            powerSet(toSelect + 1, selected + [nums[toSelect]])
            
        powerset = []
        powerSet(0, [])
        return powerset

    def bitmask(self, nums):
        # time complexity O(n2^n)
        # create a 2^n bit array
        # say S = {a,b,c,d}, bit array = [1,0,1,1] denotes subset {a,c,d}
        n = len(nums)
        powerset = []
        for i in range(2 ** n, 2 ** (n+1)):
            # generate bit mask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            # append subset corresponding to that bitmask
            powerset.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        return powerset    

    def iterative(self, nums):
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result