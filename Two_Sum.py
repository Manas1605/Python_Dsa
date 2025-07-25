

"""
LeetCode Problem 1: Two Sum


enumerate function returns the value of index with its value for ex [2,7,8]=[(0,2),(1,7)]
"""

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return (seen[diff], i)
        seen[num] = i

print(twoSum([2, 7, 11, 15], 9))
