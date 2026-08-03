class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        pf = strs[0]

        for s in strs[1:]:
            while not s.startswith(pf):
                pf = pf[:-1]
                if not pf:
                    return ""
        return pf
        