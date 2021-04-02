def findMaxConsecutiveOnes(nums):
        # iterate the list
        counter = 0
        ans = []
        for num in nums:
            # check if num in nums is 1
            if num == 1:
                # if it is counter += 1
                counter += 1
            # if it is not append counter to an empty and counter becomes 0
            else:
                ans.append(counter)
                counter = 0
        # return maximum number in the list
        ans.append(counter)
        return max(ans)


input = [1,1,0,1,1,0]
print(findMaxConsecutiveOnes(input))
