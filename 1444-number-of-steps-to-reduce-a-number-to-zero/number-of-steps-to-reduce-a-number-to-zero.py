class Solution:
    def numberOfSteps(self, num: int) -> int:
        m = 0
        i = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
                m = m+1

            else:
                num = num - 1
                m = m+1
            i = i+1
        return m
            


        