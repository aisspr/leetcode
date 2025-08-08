def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        left, max_length = 0,0

        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length