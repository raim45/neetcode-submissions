class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        start = 2
        if len(s) < 2:
            return len(s)
        for ch in range(len(s) -1, 0, -1):
            if s[ch].isalpha():
                start = ch
                break
        for ch in range(start, 0, -1):
            if s[ch].isalpha():
                res += 1
            else: 
                break
            
        return res