class Solution:
    def subsets(self, nums):
        res = []
        path = []

        def backtrack(start):
            # add current subset
            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])      # choose
                backtrack(i + 1)          # explore
                path.pop()                # un-choose

        backtrack(0)
        return res