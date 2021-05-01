class Solution(object):
    def mergeAlternately(word1, word2):
        # word1 = list(word1)
        # word2 = list(word2)

        ans = ""

        if len(word1) == len(word2):
            for w in range(len(word1)):
                ans = ans + word1[w]
                ans = ans + word2[w]
            return ans
        elif len(word1) < len(word2):
            for w in range(len(word1)):
                ans = ans + word1[w]
                ans = ans + word2[w]
            extra = (word2[len(word1):])
            ans = ans + extra
            return ans
        elif len(word1) > len(word2):
            for w in range(len(word2)):
                ans = ans + word1[w]
                ans = ans + word2[w]
            extra = (word1[len(word2):])
            ans = ans + extra
            return ans
    

    word1 = "abc" 
    word2 = "pq"
    print(mergeAlternately(word1, word2))
        