class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            # removes the lowest set bit
            n &= (n - 1)
            count += 1

        return count