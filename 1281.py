class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        x = []
        y = 0
        x += [x]
        for i in gain :
            x += [y + i]
            y = y + 1
        max = -999
        for i in x:
            if i > max:
                max = i
        return(max)