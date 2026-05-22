class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        joint = s.replace(" ", "")
        
        
        
        

        joint = joint.lower()
        nt = ""
        for ch in joint:
            if ch.isalnum():
                nt += ch
        if(len(nt) < 1):
            return True
        

        n = len(nt) // 2
        left = 0
        right = len(nt) -1
            


        for i in range(n):
            if nt[left] != nt[right]:
                return False
            left += 1
            right -= 1

        return True