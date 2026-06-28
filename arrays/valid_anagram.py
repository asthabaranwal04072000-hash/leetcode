def val_anagram(s,t):
    if len(s) != len(t):
        return False
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1 ##key,default
    for ch in t:
        if ch in count:
            count[ch] -= 1
    return not count
print(val_anagram("tan","pan"))
