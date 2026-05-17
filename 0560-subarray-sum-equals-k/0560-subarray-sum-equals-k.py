class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0

        # Stores frequency of prefix sums
        prefix_map = {0: 1}

        for num in nums:
            prefix_sum += num

            # Check if there exists a prefix sum
            # such that current_sum - previous_sum = k
            if prefix_sum - k in prefix_map:
                count += prefix_map[prefix_sum - k]

            # Store current prefix sum
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return count