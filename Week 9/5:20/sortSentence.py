class Solution:
    def sortSentence(s):
        s = s+ ' '
        word = ''
        arrayOfSentence = []
        for char in s:
            if char == ' ':
                arrayOfSentence.append(word)
                word = ''
            else:
                word = word + char
        
        dictionary = {}
        for a in arrayOfSentence:
            lastletter = a[len(a)-1]
            dictionary[lastletter] = a[0:len(a)-1]

        temp = []
        for i in sorted(dictionary.keys()):
            temp.append(dictionary[i])

        return ' '.join(temp)
    input = "is2 sentence4 This1 a3"
    print(sortSentence(input))