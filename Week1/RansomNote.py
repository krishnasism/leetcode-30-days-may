from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool: 
        ransomLetters = Counter(ransomNote)
        magLetters = Counter(magazine)
        for letter in ransomLetters:
            if ransomLetters[letter] > magLetters[letter]:
                return False
        return True
    