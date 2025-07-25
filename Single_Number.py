# xor opereator is used here
# Duplicate numbers cancel each other out, so we get the number that appears once thats why result = result ^ num only removes same element

def sum(nums):
    result = 0
    for num in nums:
        result = result ^ num
    return result
print(sum([4,1,4,1,5]))    