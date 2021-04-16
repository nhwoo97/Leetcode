class Solution(object):
    def findTheDifference(s, t):
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()

        for i in range(len(t)):
            if i == len(s):
                return t[i]
            elif s[i] == t[i]:
                continue
            else: 
                return t[i]


    input1 = "a" 
    input2 = "aa"
    print(findTheDifference(input1, input2))
