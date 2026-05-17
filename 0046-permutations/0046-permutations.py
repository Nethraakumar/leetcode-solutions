class Solution:
    def permute(self, nums):
        res = []
        used = [False] * len(nums)
        path = []

        def backtrack():
            # if permutation is complete
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # choose
                used[i] = True
                path.append(nums[i])

                # explore
                backtrack()

                # un-choose
                path.pop()
                used[i] = False

        backtrack()
        return res