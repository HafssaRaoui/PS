class Solution:
    def reverseWords(self, s: str) -> str:

        i = len(s)-1
        ans=[]

        while i >= 0 :

            #skip all spaces
            while i>=0 and s[i]==" ":
                i-=1
            
            #case space at the beginning
            if i<0:
                break
            
            #memorize the non space position
            j=i 
            while i>=0 and s[i]!=" ":
                i-=1
            
            ans.append(s[i+1:j+1])
        
        return ' '.join(ans)

#O(n) time
#O(n) extra space  (returning a new string , storing the split words in list)