class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l = [0]
        n = len(gain)
        i = 0
        while i < n:
            p = gain[i]+l[i]
            l.append(p)
            i = i+1
        
        return max(l)
        