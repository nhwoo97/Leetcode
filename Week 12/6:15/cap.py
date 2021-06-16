'''
--- Directions
    Write a function that accepts a string.  The function should
    capitalize the first letter of each word in the string then
    return the capitalized string.
--- Examples
    capitalize('a short sentence') --> 'A Short Sentence'
    capitalize('a lazy fox') --> 'A Lazy Fox'
    capitalize('look, it is working!') --> 'Look, It Is Working!'
'''
class Solution:
    def cap(str):
        newCap = ''
        for i in range(len(str)):
            if i == 0:
                newCap += str[0].capitalize()
            elif str[i - 1] == ' ':
                newCap += str[i].capitalize()
            else:
                newCap += str[i]
        return newCap

    str = 'look, it is working!'
    print(cap(str))