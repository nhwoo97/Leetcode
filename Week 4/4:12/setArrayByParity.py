class Solution(object):
    def sortArrayByParity(A):
        # using % i can find if the number is odd or even
        #two camps, odd camp and even camp
        #i add even to odd at end
        #profit
        ans = []
        even = []
        for item in A:
            if item % 2 == 1:
                ans.append(item)
            else: 
                even.append(item)
        ans = ans + even
        return ans


    input = [3,1,2,4,5]
    print(sortArrayByParity(input))