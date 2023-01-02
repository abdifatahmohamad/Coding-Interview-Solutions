class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        return self.is_all_letters_capital(word) or \
                self.is_all_letters_lower(word) or \
                self.is_title_case(word)

    
    @staticmethod
    def is_all_letters_capital(word):
        for c in word:
            if c.islower():
                return False
        return True
    
    @staticmethod
    def is_all_letters_lower(word):
        for c in word:
            if c.isupper():
                return False
        return True
    
    @staticmethod
    def is_title_case(word):
        isFirstUpper = word[0].isupper() 
        isRestLower = True
        for i in range(1, len(word)):
            if word[i].isupper():
                isRestLower = False
                
        return isFirstUpper and isRestLower 
    
    
    
    '''
        1. All letters capital 
        2. All letters are small
        3. Only the first letter is capital
        
    '''
        