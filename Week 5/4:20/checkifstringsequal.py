class Solution(object):
    def arrayStringsAreEqual(word1, word2):
        # a = ""
        # b = ""
        # for w1 in word1:
        #     a = a + w1
        # for w2 in word2:
        #     b = b + w2

        # if a == b:
        word1 = "".join(word1)
        word2 = "".join(word2)
        if word1 == word2:
            return True
        return False



    word1  = ["abc", "d", "defg"] 
    word2 = ["abcddefg"]
    print(arrayStringsAreEqual(word1, word2))