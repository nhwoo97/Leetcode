class Solution(object):
    def findNumbers(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                ans +=1
            else:
                continue 

        return ans


    input = [12,345,2,6,7896]


    print(findNumbers([12,345,2,6,7896]))
