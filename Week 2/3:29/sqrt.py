# Take x and stringify it
# Reverse the string and save it to an another variable
# Compare x and the new variable to see if its the same
#if same, return true
#if false return false
# def isPalindrome(x):
#   s = str(x)
#   rev_s = s[::-1]
#   if s == rev_s:
#     return True
#   else:
#     return False

# print(isPalindrome(121))
     

import math 


#find sqrt of x
#round the value to nearest int, but round it downwards

def sqrt(x):
  # value = math.sqrt(x)
  # ans = math.floor(value)
  # return ans
  return math.floor(math.sqrt(x))
print(sqrt(16))