class Solution(object):
    def heightChecker(heights):

        sorted_arr = sorted(heights)

        diff = 0
        
        for s in range(len(sorted_arr)):
            if sorted_arr[s] != heights[s]:
                diff +=1
            else: continue
        return diff 

    input = [1,2,3,4,5]
    print(heightChecker(input))