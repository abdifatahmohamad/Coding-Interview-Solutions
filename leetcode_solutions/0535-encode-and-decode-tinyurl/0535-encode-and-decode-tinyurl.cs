public class Codec {
    private Dictionary<string, string> encodeMap = new();
    private Dictionary<string, string> decodeMap = new();
    private const string baseUrl = "http://tinyurl.com/";
    
    // Encodes a URL to a shortened URL
    public string encode(string longUrl) {
        
        // If longUrl has been already encoded
        if(!encodeMap.ContainsKey(longUrl)){
            // Take the length of encodeMap every time and add 1 to it
            string shortUrl = baseUrl + encodeMap.Count + 1.ToString();
            
            // Take shortUrl and add it to our encodeMap
            encodeMap[longUrl] = shortUrl;
            // Take longUrl and add it to our decodeMap
            decodeMap[shortUrl] = longUrl;
        }
        
        // If already encoded, then return that encoded longUrl
        return encodeMap[longUrl];
        
    }

    // Decodes a shortened URL to its original URL.
    public string decode(string shortUrl) {
        // Take the shortUrl that is been already encoded, and then decode & return it
        return decodeMap[shortUrl];   
        
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));
