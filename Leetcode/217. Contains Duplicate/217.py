
#! Brutforce approach
def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    
    return False


a = containsDuplicate([1,2,3,4,5,1])
b = containsDuplicate([1,2,3,4])
print(a)
print(b)

#! TLE
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False