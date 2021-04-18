class Solution(object):
    def canConstruct(ransomNote, magazine):
        list(ransomNote).sort()
        list(magazine).sort()

        mdict = {}

        for m in magazine:
            if m in mdict.keys():
                newValue = mdict[m] + 1
                mdict[m] = newValue
            else: 
                mdict[m] = 1
                
        for r in ransomNote:
            if r in mdict.keys():
                if mdict[r] == 1:
                    mdict.pop(r)
                else:
                    newValue = mdict[r] - 1
                    mdict[r] = newValue
            else:
                return False
        return True

    input1 = "a"
    input2 = "aab"
    print(canConstruct(input1,input2))