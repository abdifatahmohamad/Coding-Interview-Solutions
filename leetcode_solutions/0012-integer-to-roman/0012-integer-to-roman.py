class Solution:
    def intToRoman(self, num: int) -> str:
        # symbol = {
        #     "I": 1,
        #     "IV": 4,
        #     "V": 5,
        #     "IX": 9,
        #     "X": 10,
        #     "XL": 40
        #     "L": 50,
        #     "XC": 90,
        #     "C": 100,
        #     "CD": 400,
        #     "D": 500,
        #     "CM": 900,
        #     "M": 1000
        # }
        
        symbol = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000]
        ]
        
        res = ""
        for sym, val in rev_symbol(symbol):
            '''
            let's say we have 900,
            count = 900 // m(1000) = 0 --> that means 0m goes to the res
            res += m * count(0)
            count = 900 // cm(900) = 1 -> that means 1cm goes to the res
            res += cm * count(1)
            
            '''
            count = num // val
            res += sym * count
            num =  num % val
        return res
        
# Traverse list of symbols and their values backwards       
def rev_symbol(sym):
    return [sym[i] for i in range(len(sym) - 1, -1, -1)]
        
        
        
        
        
        
        
        
        
        
        
        
    
        