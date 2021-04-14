class Solution(object):
    def reformat(s):
        #we will separate s into two different array, one will be for char, the other for num
        #compare the len of char and int to figure out if this will be possible
        #if possible, proceed, if not, return empty string
        #use loop to add one of char, then int, etc

        char = []
        num = []

        for i in s:
            if i.isalpha():
                char.append(i)
            else:
                num.append(i)
        ans = ""
        # C N C N C char ALWAYS STARTS FIRST IN THIS CASE
        if len(char) == len(num) or abs(len(char) - len(num)) == 1:
            if len(char) > len(num):
                for a in range(len(num)):
                    ans = ans + char[a]
                    ans = ans + num[a]
                ans = ans + char[len(char) - 1]
            elif len(char) < len(num):
                for a in range(len(char)):
                    ans = ans + num[a]
                    ans = ans + char[a]
                ans = ans + num[len(num) - 1]
            else:
                for a in range(len(num)):
                    ans = ans + char[a]
                    ans = ans + num[a]
            return ans
        else:
            return ""

    input = "covid2019"
    print(reformat(input))



    