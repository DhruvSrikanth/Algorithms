# Time complexity is normally O(m*n*2^(m+n)) but with dp becomes O(m*n)

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    if m == 0 or n == 0:
        return 0
    else:
        if X[m] == Y[n]:
            return 1 + lcs(X[:-1], Y[:1])
        else:
            return max(lcs(X[:-1],Y), lcs(X, Y[:-1]))

def lcs_dp(X , Y):
    m = len(X)
    n = len(Y)
 
    L = [[0]*(n+1) for i in range(m+1)]
 
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(1, m+1):
        for j in range1, (n+1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
 
 
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs_dp(X, Y))
