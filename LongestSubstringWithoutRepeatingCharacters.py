def longestSubstringWithoutRepeatingCharacters(s):
    mySet = set()
    ans = i = j = 0
    while i < len(s) and j < len(s):
        if s[j] not in mySet:
            mySet.add(s[j])
            j += 1
            ans = max(ans, j - i)
        else:
            mySet.remove(s[i])
            i += 1
    return ans
    

if __name__ == '__main__':
    s = "abcabcbb"
    print(longestSubstringWithoutRepeatingCharacters(s))
