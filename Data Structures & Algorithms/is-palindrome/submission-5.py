class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        l = 0
        r = len(s) - 1

        for i in range((len(s) + 2 - 1) // 2):
            if s[l + i] == s[r - i]:
                continue
            return False
        return True