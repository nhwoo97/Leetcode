class Solution(object):
    def reverse(sentence):
        
        if x < 0:
            x = str(x)[::-1]
            x = x[0:len(x)-1]
            x = -abs(int(x))
        else:
            x = int(str(x)[::-1])
        if -2**31 < x and x < 2**31 - 1:
            return x
        return 0

    