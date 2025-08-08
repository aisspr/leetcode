def compress(self, chars: List[str]) -> int:
        
        n = len(chars)
        if n <= 1:
            return n
        read, write = 0,0

        while read < n:
            current_char = chars[read]
            cnt = 0
            while read < n and chars[read] == current_char:
                cnt += 1
                read += 1
            chars[write] = current_char
            write += 1
            if cnt > 1:
                cnt_str = str(cnt)
                for digit_char in cnt_str:
                    chars[write] = digit_char
                    write += 1
        return write