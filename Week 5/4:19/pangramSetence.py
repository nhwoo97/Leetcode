class Solution(object):
    def checkIfPangram(sentence):
        alph = 'abcdefghijklmnopqrstuvwxyz'
        alph = list(alph)

        sentence = list(set(sentence))
        sentence.sort()

        if alph == sentence:
            return True
        return False

        


    input = "uwqohxamknblecdtzpisgvyfjr"
    print(checkIfPangram(input))