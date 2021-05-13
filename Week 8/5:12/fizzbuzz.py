class Solution:
    def fizzBuzz(n):

        newArr = []
        i = 1
        while i < n + 1 :
            if i % 3 == 0 and i % 5 == 0:
                newArr.append('FizzBuzz')
                i += 1
            elif i % 3 == 0:
                newArr.append('Fizz') 
                i += 1
            elif i % 5 == 0:
                newArr.append('Buzz') 
                i += 1
            else:
                newArr.append(str(i))
                i += 1
        return newArr
    input = 15
    print(fizzBuzz(input))
        