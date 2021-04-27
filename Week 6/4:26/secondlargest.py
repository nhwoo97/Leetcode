class Solution(object):
    def secondHighest(s):
        numsOnly = []
        for i in s:
            if i.isalpha():
                continue
            else:
                numsOnly.append(int(i))
        
        numsOnly.sort(reverse=True)

        if numsOnly[0] == numsOnly[1]:
            return -1
        if len(numsOnly) < 2:
            return -1

        return numsOnly[1]

    input = "abc1111"
    print(secondHighest(input))