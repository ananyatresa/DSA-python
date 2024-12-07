class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        left=0
        n =len(s)
        charset=set()
        for right in range(n):
            if s[right] not in charset:
                charset.add(s[right])
                max_length =max(max_length, right-left+1)
            else:
                while(s[right] in charset):
                    charset.remove(s[left])
                    left+=1
                charset.add(s[right])
        return max_length

obj_sol = Solution()
print(obj_sol.lengthOfLongestSubstring("aaaaabcd"))