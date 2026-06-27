def contains_dup(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
print(contains_dup([1,3,1,2]))