class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1) == 0 or len(s2) < len(s1)):
            return False
        perm = [0]*26
        l = 0
        
        for i in range(len(s1)):
            perm[ord(s1[i]) - ord("a")] += 1 
        comp = [0]*26
        for r in range(len(s2)):
            comp[ord(s2[r]) - ord("a")] += 1
            if r - l +1 > len(s1):
                comp[ord(s2[l]) - ord("a")] -= 1
                l += 1

            
            if comp == perm:
                return True
        return False
                

        