class Solution(object):
    def sumOfUnique(nums):
        newArr = []
        ans = 0
        for n in nums:
            if n in newArr:
                continue
            else:
                newArr.append(n)
                ans = ans + n
        return ans

        # hashmap = {}
        # for i in nums:
        #     if i in hashmap.keys():
        #         hashmap[i] += 1
        #     else:
        #         hashmap[i] = 1
        # sum = 0
        # for k, v in hashmap.items():
        #     if v == 1: sum += k
        # return sum

    input = [1,2,3,4,5]
    print(sumOfUnique(input))
    