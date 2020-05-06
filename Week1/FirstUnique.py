class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
            i += 1
        return -1
        