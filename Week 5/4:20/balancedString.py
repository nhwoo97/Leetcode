class Solution(object):
    def balancedStringSplit(s):

#Either L or R
        ans = 0
        mydict = {
            "L" : 0,
            "R" : 0
        }
        for string in range(len(s)):
            # Checking if this is the first value
            if mydict['L'] == 0:
                if s[string] == "L":
                    newValue = mydict["L"] + 1
                    mydict["L"] = newValue 
                if s[string] == "R":
                    newValue = mydict["R"] + 1
                    mydict["R"] = newValue 
            #everything after first one
            else:
                if s[string] != s[string - 1]:
                    ans += 1
                    mydict.clear()
                    mydict = {"L" : 0, "R" : 0}
        return ans

    input = "RLRL"
    print(balancedStringSplit(input))