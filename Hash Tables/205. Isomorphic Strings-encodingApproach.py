class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def encode(string):

            encoded = []
            map = {}

            for index,char in enumerate(string):
                if char not in map:
                    map[char] = index
                
                encoded.append(map[char])
            
            return encoded

        return encode(s) == encode(t)


# Basic intuition on seriliazing both strings and comparing them      
# it works because we track first occurence of each character 
        
                
                


            