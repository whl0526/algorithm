class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        
        char = list(s)
        
        start = 0
        end = len(s) - 1 #인덱스 값은 0부터 시작이기 때문에
        
        while start < end: 
            minChar = min(char[start], char[end])
            char[start] = minChar
            char[end] = minChar
            
            start += 1
            end -= 1
            
        return ''.join(char)
            
        
        
        
        
        