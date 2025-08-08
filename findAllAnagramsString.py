def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        len_s = len(s)
        len_p = len(p)

        if len_s < len_p:
            return []

        result_idx = []
        p_counts = Counter(p)

        s_window_counts = Counter(s[:len_p])
        if p_counts == s_window_counts:
            result_idx.append(0)
        
        for left in range(1, len_s-len_p+1):
            char_to_remove = s[left-1]
            s_window_counts[char_to_remove] -= 1
            if s_window_counts[char_to_remove] == 0:
                del s_window_counts[char_to_remove]
            char_to_add = s[left + len_p-1]
            s_window_counts[char_to_add] += 1

            if p_counts == s_window_counts:
                result_idx.append(left)
        return result_idx