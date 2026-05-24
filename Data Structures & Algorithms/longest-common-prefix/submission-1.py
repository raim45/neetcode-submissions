class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        val, val1, val2 = "", "", ""
        for ch in strs[0]:
            val1 += ch
        
        for ch in strs[-1]:
            val2 += ch

        
        for i in range(min(len(val1), len(val2))):
            if val1[i] == val2[i]:
                val += val1[i]
            else:
                break
    
        return val

