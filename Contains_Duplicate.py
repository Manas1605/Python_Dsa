def Contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False
print(Contains_duplicate([1,2,3,4]))