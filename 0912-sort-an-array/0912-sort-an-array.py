class Solution:
    def sortArray(self, nums):
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

    def merge_sort(self, nums, left, right):
        if left >= right:
            return

        mid = (left + right) // 2

        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        left_part = nums[left:mid + 1]
        right_part = nums[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                nums[k] = left_part[i]
                i += 1
            else:
                nums[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            nums[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            nums[k] = right_part[j]
            j += 1
            k += 1