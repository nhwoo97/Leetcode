class Solution(object):
    def reverseOnlyLetters(S):

        abcs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' , 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        stringOnly = []
        for char in S:
            if char in abcs:
                stringOnly.append(char)
            else:
                continue
        stringOnly.reverse()
        
        counter = 0
        ans = ""
        for item in S:
            if item in abcs:
                ans = ans + stringOnly[counter]
                counter =  counter + 1
            else:
                ans = ans + item
        return ans

    input = "a-bC-dEf-ghlj"
    print(reverseOnlyLetters(input))

        