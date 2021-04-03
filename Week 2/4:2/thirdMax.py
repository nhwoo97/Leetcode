class Solution(object):
    def thirdMax(nums):
        # sort the list
        #choose s[2]
        if len(nums) < 3:
            nums.sort(reverse=True)
            return nums[0]
        noDuplicate = list(set(nums))
        noDuplicate.sort(reverse=True)
        if len(noDuplicate) < 3:
            return noDuplicate[0]
        return noDuplicate[2]


    
    input = [1,1,2]
    print(thirdMax(input))