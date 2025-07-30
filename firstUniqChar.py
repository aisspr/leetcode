def firstUniqChar(self, s: str) -> int:
        counts = [0]*26

        for c in s:
            counts[ord(c)-ord('a')] += 1

        for i, c in enumerate(s):
            if counts[ord(c)-ord('a')] == 1:
                return i
        return -1