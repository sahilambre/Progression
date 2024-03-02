def reverseArray(nums):
    newList = []
    for i in range(len(nums) - 1, -1, -1):
        newList.append(nums[i])
    return newList

print(reverseArray([1,2,3,4,5,6]))
