
import bisect

def lengthOfLIS(nums):
    # time complexity O(n^2)
    # [10,9,2,5,3,7,101,18]
    # [ 1,1,1,2,2,3,  4, 4]
    LIS = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                LIS[i] = max(LIS[i], LIS[j] + 1)
    print('LIS = ', LIS)
    return max(LIS)

# time complexity O(nlogn): binary search (patience sorting)
def lenOfLIS(nums):
    piles = []
    for card in nums:
        pile = bisect.bisect_left(piles, card)
        if pile == len(piles):
            piles.append(card)
        else:
            piles[pile] = card
    print('pile = ', piles)
    return len(piles)

# test case
n = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(n))
print(lenOfLIS(n))