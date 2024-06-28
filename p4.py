class Solution(object):
    def wordBreak(self,s, wordDict):
        s = s.lower()
        
        wordDict = set(word.lower() for word in wordDict)


        memo = {}

        def backtrack(start):
            if start in memo:
                return memo[start]


            result = []
            if start == len(s):
                result.append("")

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordDict:
                    sub_sentences = backtrack(end)
                    for sub_sentence in sub_sentences:
                        if sub_sentence:
                            result.append(word + " " + sub_sentence)
                        else:
                            result.append(word)

            memo[start] = result
            return result

        return backtrack(0)




s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
sol = Solution()
print(sol.wordBreak(s, wordDict))
