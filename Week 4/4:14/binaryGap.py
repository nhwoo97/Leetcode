class Solution(object):
    def binaryGap(n):
        binary = list(bin(n))
        points = []
        for b in range(len(binary)):
            if binary[b] == "1":
                points.append(b)
            else:
                continue
        max = 0
        for p in range(len(points)):
            if p == 0:
                continue
            else:
                bslice = slice(points[p-1], points[p])
                temp = binary[bslice]
                lengtho = len(temp)
                if max < lengtho:
                    max = lengtho
                else:
                    continue
        return max
    input = 6
    print(binaryGap(input))
        