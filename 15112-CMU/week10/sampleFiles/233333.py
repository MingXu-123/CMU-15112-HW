def substrCount(n, s):
    counter = 0
    # following code count palindrome len of Palindrome str longer than 2
    for i in range(n):
        offset = 1
        while i - offset >= 0 and i + offset < n:
            if offset >= 2:
                if s[i - offset] == s[i + offset] and \
                s[i - offset] == s[i - 1] and s[i + offset] == s[i - 1]:
                    counter += 1
                    offset += 1
                    continue
                else:
                    break
            if offset == 1:
                if s[i - offset] == s[i + offset]:
                    counter += 1
                    offset += 1
                    continue
                else:
                    break
    # following code counter repeats like "aa"
    repeats = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            repeats += 1
    res = counter + repeats + n # n is the palindrome with len 1
    for i in range(len(s)):
        length = 0
        while s[i + length] == s[i]:
            length += 1

    return res
print(substrCount(4, "aaaa"))
print(substrCount(7, "abcbaba"))
