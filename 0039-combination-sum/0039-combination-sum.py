class Solution:
    def combinationSum(self, candidates, target):
        res = []
        path = []

        def backtrack(start, total):
            # if we reach target
            if total == target:
                res.append(path[:])
                return

            # if we exceed target, stop
            if total > target:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                # choose
                path.append(num)

                # reuse same number allowed → pass i (not i+1)
                backtrack(i, total + num)

                # un-choose
                path.pop()

        backtrack(0, 0)
        return res