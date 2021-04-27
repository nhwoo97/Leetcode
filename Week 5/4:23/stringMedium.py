class Solution(object):
    def wordSubsets(A, B):

        # Iterate through B and make sure that it's one letter for each
        newB = []
        for Bthing in B:
            if len(Bthing) > 1:
                tempArr = list(Bthing)
                newB = newB + tempArr
            else:
                newB.append(Bthing)

        ans = []

        for Aword in A:
            tempB = newB[:]
            for a in Aword:
                if a in tempB:
                    tempB.remove(a)
            # return len(tempB)
            if len(tempB) < 1:
                ans.append(Aword)
        return ans
            
            

    A = ["amazon","apple","facebook","google","leetcode"]
    B = ["e","oo"]

    print(wordSubsets(A, B))