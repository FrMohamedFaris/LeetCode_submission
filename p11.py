from collections import defaultdict
class Solution(object):
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        word_length = len(words[0])
        total_length = len(words[0]) * len(words)
        word_count = defaultdict(int)

        for word in words:
            word_count[word] += 1

        result = []

        for i in range (len(s) - word_length + 1):
            for i in range(len(s) - total_length + 1):
                seen = defaultdict(int)
                j = 0
                while j < len(words):
                    word = s[i + j * word_length: i + (j + 1) * word_length]
                    if word in word_count:
                        seen[word] += 1
                        if seen[word] > word_count[word]:
                            break
                    else:
                        break
                    j += 1
                if j == len(words):
                    result.append(i)

            return result


s = "barfoothefoobarman"
words = ["foo", "bar"]

sol = Solution()
print(sol.findSubstring(s,words))
