class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        m = M = 0
        for i in nums:
            if i:
                m += 1
            else:
                if M < m:
                    M = m
                m = 0
        if M < m:
            return m
        return M
