class Solution(object):
    def isAnagram(s, t):
        #check if the length is the same
        if len(s) != len(t):
            return False
        if sorted(list(s)) == sorted(list(t)):
           return True
        return False
    

    s = "apple"
    t = "lapep"
    print(isAnagram(s,t))