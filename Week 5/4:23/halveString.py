class Solution(object):
    def halvesAreAlike(s):
        myDic = {"a":0, "b":0}
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for string in range(len(s)):
            if string < (len(s))/2:
                if s[string] in vowels:
                    temp = myDic['a'] + 1
                    myDic['a'] = temp
                else: 
                    continue
            else:
                if s[string] in vowels:
                    temp = myDic['b'] + 1
                    myDic['b'] = temp
                else:
                    continue
        if myDic['a'] == myDic['b']:
            return True
        return False
        

    s = "AbCdEfGh"
    print(halvesAreAlike(s))