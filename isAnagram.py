def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_cnt, t_cnt = {}, {}

        for char in s:
            s_cnt[char] = s_cnt.get(char, 0) + 1
        for char in t:
            t_cnt[char] = t_cnt.get(char,0) + 1
        return s_cnt == t_cnt