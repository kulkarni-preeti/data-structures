def mergeAlternately(self, word1, word2):
    n,m = len(word1), len(word2)
    r = max(m,n)
    res = []
    for i in range(r):
        if i < n:
            res.append(word1[i])
        if i < m:
            res.append(word2[i])
    return "".join(res)