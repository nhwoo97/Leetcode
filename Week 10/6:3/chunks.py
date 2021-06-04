# // --- Directions
# // Given an array and chunk size, divide the array into many subarrays
# // where each subarray is of length size
# // --- Examples
# // chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
# // chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
# // chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
# // chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
# // chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

class Solution:
    def ch(c, s):
        counter = 0
        final = []
        temp = []

        for i in range(len(c)):
            if counter < s:
                temp.append(c[i])
                counter +=1
            else:
                final.append(temp)
                temp = []
                counter = 0
                temp.append(c[i])
                counter += 1
                
        if len(temp) > 0:
            final.append(temp)

        return final



    print(ch([1, 2, 3, 4], 2))