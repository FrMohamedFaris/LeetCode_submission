from collections import Counter


class Solution(object):
    def commonChars(self, words):
        min_freq = Counter(words[0])

        for word in words[1:]:
            word_freq = Counter(word)
            for char in min_freq:
                min_freq[char] = min(min_freq[char], word_freq[char])

        result = []
        for char, freq in min_freq.items():
            result.extend([char] * freq)

        return result


words = ["bella", "label", "roller"]
sol = Solution()
print(sol.commonChars(words))
