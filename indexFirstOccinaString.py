def strStr(self, haystack: str, needle: str) -> int:
    n = len(haystack)
    m = len(needle)

    if m > n:
        return -1
    for i in range(n-m+1):
        match = True
        for j in range(m):
            if haystack[i+j] != needle[j]:
                match = False
                break
        if match:
            return i
    return -1