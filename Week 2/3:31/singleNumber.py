def singleNumber(nums):
  # iterate through nums and assign to dic 
  dict = {}
  for num in nums:
    if num in dict:
      frq = dict[num]
      added = frq + 1
      dict[num] = added
    else:
      dict[num] = 1
  
  for a in dict:
    if dict[a] == 1:
      return a
    else:
      continue
  
  

input = [4 , 1 , 2, 1, 2]

print(singleNumber(input))