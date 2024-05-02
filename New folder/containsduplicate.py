def containsduplicate(nums):
    nums.sort()
    n = len(nums)
    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            return True
    return False

nums = list(map(int, input().split()))
a = containsduplicate(nums)
print(a)

        
