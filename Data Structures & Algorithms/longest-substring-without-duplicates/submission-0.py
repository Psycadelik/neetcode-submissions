class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_chars = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in window_chars:
                window_chars.remove(s[left])
                left += 1

            window_chars.add(s[right])
            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length
