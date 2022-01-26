# Time complexity is normally O(2^(m+n)) but with dp becomes O(m*n)

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    if m == 0 or n == 0:
        return 0
    else:
        if X[m] == Y[n]:
            return 1 + lcs(X[:-1], Y[:-1])
        else:
            return max(lcs(X[:-1],Y), lcs(X, Y[:-1]))

def lcs_dp(X , Y):
    m = len(X)
    n = len(Y)
 
    L = [[0]*(n+1) for i in range(m+1)]
 
    for i in range(1, m+1):
        for j in range1, (n+1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    return L[m][n]
 
 
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs_dp(X, Y))




'''

Proof of correctness:

We will use a proof by strong induction on length.

Basis - 

i = 0 or j = 0, meaning C[i,j] = 0, where C[i,j] provides the length of the longest subsequence for the given strings till i and j respectively.

This completes our basis step.

Inductive Step - 
IH - Assume claim on C[i',j'] providing the length of the longest subsequence for i' and j' is true for i' + j' < i + j.

Let Z be the LCS of X[1..i], Y[1..j].
Case 1 - If X[i] = Y[j], then the previous Z that had X[i]= Y[j], so C[i-1,j-1] + 1 is the new LCS. We know by the IH C[i-1,j-1] is correct therefore, our new LCS is correct.

Case 2 - When X[i] is not equal to Y[j], then the new LCS does not change from the old one, therefore, we take the max of C[i-1,j] and C[i,j-1]. By the IH, we know that C[i-1,j] and C[i,j-1] are correct.

This completes our inductive step.

Therefore, by strong induction on the length, we have shown that our algorithm is correct.

'''
