class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        from collections import Counter

        need = Counter(t)
        window = {}

        have = 0
        need_count = len(need)

        left = 0
        res = (float("inf"), 0, 0)

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == need_count:
                # update result
                if (right - left + 1) < res[0]:
                    res = (right - left + 1, left, right)

                # shrink window
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        return "" if res[0] == float("inf") else s[res[1]:res[2] + 1]