def knuthMorrisPrattSearch(text: str, pattern: str) -> bool:
    lps = [0] * len(pattern)

    def fill_longest_prefix_suffix():
        j = 1
        i = 0
        nonlocal lps
        while j < len(pattern):
            if pattern[i] == pattern[j]:
                i += 1
                lps[j] = i
                j += 1
            else:
                if i != 0:
                    i = lps[i - 1]
                else:
                    j += 1

    fill_longest_prefix_suffix()
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == len(pattern):
                return True
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False

        