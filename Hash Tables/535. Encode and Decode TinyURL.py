import random 
import string
class Codec:


    def __init__(self):
        self.base_url = "http://tinyurl.com/"
        self.key_length = 6 
        self.secret = {}
        self.charset = string.ascii_letters + string.digits
    

    def generate_key(self):
        return ''.join(random.choice(self.charset) for _ in range(self.key_length))
    
    def encode(self, longUrl: str) -> str:

        key = self.generate_key()
        while key in self.secret:
            key = self.generate_key()
        
        self.secret[key] = longUrl
        return self.base_url+key
    


    def decode(self, shortUrl: str) -> str:

        #extract the key
        key = shortUrl.replace(self.base_url,"")
        return self.secret.get(key,"")

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


# Time Complexity: 
# Encoding: O(1) in the average case, O(n) for collision resolution.
# Decoding: O(1) as dictionary lookup is constant time.

# Space Complexity: O(n) where n is the number of unique URLs that have been encoded.

