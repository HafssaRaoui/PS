class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        #do xor to every number
        xor = 0 
        for num in nums :
            xor^=num
        
        bit_diff = 1
        #using & find the bit diff
        while not bit_diff & xor :
            bit_diff =  bit_diff << 1
        

        a,b = 0,0
        for num in nums :
            if num & bit_diff :
                a^= num
            
            else:
                b^= num
        return [a,b]

