import string
class Codec : 

    def __init__(self):
        
        self.base_url = "http://tinyurl.com/"
        self.counter = 0 # variable to increment the id
        self.id_to_url = {}
        self.url_to_id = {}
        self.charset = string.ascii_letters + string.digits
    


    #123 -> 'b9'
    def _endode_id(self,id):

        if id == 0 : 
            return self.charset[0]
        
        base_62 = []
        while id : 

            id,rem = divmod(id,62)
            base_62.append(self.charset[rem])
        
        return ''.join(reversed(base_62))
    
    #'b9' -> 123

    def _decode_id(self,base_62_):
        
        for char in base_62_ : 
            id = id*62 + self.charset.index(char)
        
        return id

    def encode(self, longUrl: str) -> str:

        if longUrl in self.url_to_id:
            id = self.url_to_id[longUrl]

        else :
            #generate an id to be encoded 
            self.counter += 1 
            id = self.counter
            self.id_to_url[id] = longUrl
            self.url_to_id[longUrl] = id

    
        return self.base_url + self._endode_id(id)

    def decode(self, shortUrl: str) -> str:
        # extract the encoded id part 
        id = shortUrl.replace(self.base_url,"")

        return self.id_to_url.get(self._decode_id(id),"")

# Time Complexity: 
# Encoding: O(log(n)) due to base conversion, where n is the number of URLs.
# Decoding: O(log(n)) for the reverse conversion.

# Space Complexity: O(n), where n is the number of unique URLs stored.

