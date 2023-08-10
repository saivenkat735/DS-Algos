def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
    
    # Initialize a 2D table to store LCS lengths
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Backtrack to find the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))

# Example usage
sequence1 = "ABCBDAB"
sequence2 = "BDCAB"
result = longest_common_subsequence(sequence1, sequence2)
print("Longest Common Subsequence:", result)
