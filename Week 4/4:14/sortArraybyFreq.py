class Solution(object):
    def frequencySort(nums):
        #use dic where key is the frequency and the values are the numbers
        #iterate through the dictionary to create an array where it is done based on increasing order, if the frequency is the same, do it based on descending order
        # freq = {}
        # for num in nums:
        #     if (num in freq):
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1
        # sortedFreq = sorted(freq key=freq.items())
        # return sortedFreq
        rev_sorted = sorted(nums,reverse=1)
        # nums.count counts how many of them exists
        return sorted(rev_sorted, key=nums.count)

    input = [1,1,2,2,2,3]
    print(frequencySort(input))
        