class Solution(object):
    def truncateSentence(s, k):
        newList = list(s.split())
        ans = ""
        for i in range(k):
            ans = ans+ " " + newList[i]
        return ans
        

    s = "Hello how are you Contestant" 
    k = 4
    print(truncateSentence(s, k))