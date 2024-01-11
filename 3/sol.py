class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        left = 0
        seen = set()
        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
            else:
                ans = max(ans, right - left)
                while(s[left] != s[right]):
                    seen.remove(s[left])
                    left += 1
                left += 1
        ans = max(ans, len(s) - left)
        return ans