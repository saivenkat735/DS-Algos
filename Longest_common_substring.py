def longest_common_substring(X, Y):
    m = len(X)
    n = len(Y)
    
    # Initialize a 2D table to store lengths of common substrings
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Variables to store the maximum length and its ending position
    max_length = 0
    ending_pos = 0
    
    # Fill the table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    ending_pos = i
    
    # Extract the longest common substring
    longest_common_substring = X[ending_pos - max_length: ending_pos]
    
    return longest_common_substring

# Example usage
string1 = "ABCBDAB"
string2 = "BDCAB"
result = longest_common_substring(string1, string2)
print("Longest Common Substring:", result)
