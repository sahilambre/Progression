def twoSum(nums, target):
    n = len(nums)
    two_sum = []
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                two_sum.append(i)
                two_sum.append(j)

                return two_sum
            

input1 = [2,7,5,11]
expectedOutput = 9

print(twoSum(input1, expectedOutput))