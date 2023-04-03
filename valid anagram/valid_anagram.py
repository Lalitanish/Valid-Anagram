class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        for letter in s:
            if letter not in dict1:
                dict1[letter] = 1
            else:
                dict1[letter] += 1

        for letter in t:
            if letter not in dict1:
                return False
            else:
                dict1[letter] -= 1

        for values in dict1.values():
            if values != 0:
                return False
        return True
