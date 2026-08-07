class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # ans = 0
        # s = s.strip()

        # for i in range(len(s)-1,-1,-1):

        #     if s[i] == " ":
        #         break
        #     ans +=1
        
        # return ans

        i = len(s) - 1

        while i >= 0 and s[i] == " ":
            i -= 1

        ans = 0
        while i >= 0 and s[i] != " ":
            ans += 1
            i -= 1

        return ans