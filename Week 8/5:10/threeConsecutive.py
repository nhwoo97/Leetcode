class Solution:
    def threeConsecutiveOdds(arr):
        counter = 0
        for a in arr:
            if a % 2 == 1:
                counter += 1
                if counter == 3:
                    return True
            else:
                counter = 0
        return False
    input = [1,2,34,3,4,5,7,23,12]
    print(threeConsecutiveOdds(input))