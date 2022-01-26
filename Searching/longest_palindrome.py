def longestPalindrome(text):
    ntext = f'|{"|".join(list(text))}|'
    PalindromeRadii = [0] * len(ntext)

    center = 0
    radius = 0

    while center < len(ntext):
        while center - (radius + 1) >= 0 and center + (radius + 1) < len(ntext) and ntext[center - (radius + 1)] == ntext[center + (radius + 1)]:
            radius += 1

        PalindromeRadii[center] = radius

        oldcenter = center
        oldradius = radius

        center = center + 1
        radius = 0

        while center <= oldcenter + oldradius:
            mirroredcenter = oldcenter - (center - oldcenter)
            maxmirroredradius = oldcenter + oldradius - center
            if PalindromeRadii[mirroredcenter] < maxmirroredradius:
                PalindromeRadii[center] = PalindromeRadii[mirroredcenter]
                center += 1
            elif PalindromeRadii[mirroredcenter] > maxmirroredradius:
                PalindromeRadii[center] = maxmirroredradius
                center += 1
            else:
                radius = maxmirroredradius
                break
    longest_palindrome_in_ntext = 2 * max(PalindromeRadii) + 1
    longest_palindrome_in_text = (longest_palindrome_in_ntext - 1)//2
    return longest_palindrome_in_text


def main():
    print(longestPalindrome('abacaba'))


if __name__ == '__main__':
    main()
