charMap = [0] * 26
def verifyingAlienDictionary(words, order):
    for i in range(len(order)):
        charMap[ord(order[i]) - ord('a')] = i
    print(charMap)

    for i in range(0, len(words) - 1):
        if compare(words[i], words[i+1]) > 0:
            return False
    return True


def compare(word1, word2):
    i = j = val = 0
    while word1 and word2 and val == 0:
        val = charMap[ord(word1[i])- ord('a')] - charMap[ord(word2[j])- ord('a')]
        i += 1
        j += 1
    if val is 0:
        return len(word1) - len(word2)
    else:
        return val

if __name__ == '__main__':
    words = ["word", "world", "row"]
    order = "worldabcefghijkmnpqstuvxyz"
    print(verifyingAlienDictionary(words,order))
