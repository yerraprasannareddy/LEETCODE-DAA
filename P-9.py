def longestCommonSubsequence(text1, text2):
    len1, len2 = len(text1), len(text2)
 
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
 
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:   
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
 
    return dp[len1][len2]
 
text1 = "abcde"
text2 = "ace"
result = longestCommonSubsequence(text1, text2)
print(f"Length of the Longest Common Subsequence: {result}")
