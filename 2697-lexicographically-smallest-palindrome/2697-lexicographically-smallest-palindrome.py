class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        char = list(s)
        i = 0
        j = len(s) - 1 #인덱스 값은 0부터 시작이기 때문에
        
        while i < j: 
            minChar = min(char[i], char[j])
            char[i] = minChar
            char[j] = minChar
            
            i += 1
            j -= 1
            
        return ''.join(char)
            
        
        
        
        
        