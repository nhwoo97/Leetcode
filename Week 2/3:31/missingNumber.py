def missingNumber(nums):
  nums.sort()
  if nums[0] == 0 and len(nums) == 1:
    return 1
  if nums[0] == 1 and len(nums) == 1:
    return 0
  counter = nums[0]
  for n in nums:
    if n != counter:
      return counter 
    else:
      counter += 1
      continue
  return nums[len(nums)-1] + 1
nums = [0,1]
print(missingNumber(nums))