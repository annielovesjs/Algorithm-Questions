class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True #null character
        for i in range(1, len(s) + 1):
            j = 0
            while j < i:
                if dp[j] and s[j:i] in wordDict:
                    print(s[j:i])
                    dp[i] = True
                    break
                j+=1
        return dp[len(s)]