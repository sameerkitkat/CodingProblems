def partitionLabels(s):
    myDict = {c : i for i,c in enumerate(s)}
    j = anchor = 0
    ans = []
    for i, c in enumerate(s):
        j = max(j, myDict[c])
        if i == j:
            ans.append(i - anchor + 1)
            anchor = i + 1
    return ans


if __name__ == '__main__':
    s = 'ababcbacadefegdehijhklij'
    print(partitionLabels(s))
