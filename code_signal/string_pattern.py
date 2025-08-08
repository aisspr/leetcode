#string pattern

def isAnagram(s,t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

def samePattern(s,t):
    if len(s) != len(t):
        return False
    
    def _getPattern(word):
        mapping = {}
        pattern = []
        next_id = 0
        for c in word:
            if c not in mapping:
                mapping[c] = next_id
                next_id += 1
            pattern.append(mapping[c])
        return pattern
    return _getPattern(s) == _getPattern(t)
