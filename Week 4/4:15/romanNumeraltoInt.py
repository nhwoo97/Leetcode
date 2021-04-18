class Solution(object):
    def romanToInt(s):
        """

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

        """
        # 4 IV and 9 IX
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        s = list(s)
        ans = 0
        for i in range(len(s)):
            if s[i] == "I":
                ans += 1
            elif s[i] == "V":
                ans += 5
            elif s[i] == "X":
                ans += 10
            elif s[i] == "L":
                ans += 50
            elif s[i] == "C":
                ans += 100
            elif s[i] == "D":
                ans += 500
            elif s[i] == "M":
                ans += 1000
        return ans
    input = "MCMXCIV"
    print(romanToInt(input))
            