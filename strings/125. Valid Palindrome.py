class Solution:
    def isPalindrome(self, s: str) -> bool:

        ps=''

        for char  in s : 
            ch =char.lower()
            if 'a'<=ch<='z' or '0'<=ch<='9':
                ps+=ch
        
        l,r = 0 , len(ps)-1

        while l < r:
            if ps[l]!=ps[r]:
                return False

            l+=1
            r-=1
        
        return True

# O(n) extra space