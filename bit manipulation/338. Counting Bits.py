class Solution:
    def countBits(self, n: int) -> List[int]:


        output = [0]*(n+1)
        for i in range(1,n+1):
            count = 0
            q=i

            while q!=0:
                if q%2 == 1 :
                    count+=1
                
                q//=2
            
            output[i] = count
        
        return output