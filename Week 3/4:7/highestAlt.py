class Solution(object):
    def largestAltitude(gain):
        placements = []
        
        for g in range(len(gain)):
            if g == 0:
                placements.append(gain[g])
            else:
                current = placements[g-1] + gain[g]
                placements.append(current)

        if max(placements) < 0:
            return 0
        else:
            return max(placements)

    
    input = [-4,-3,-2,-1,4,3,2]
    print(largestAltitude(input))