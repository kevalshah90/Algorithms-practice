class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Counter variable
        c = 0
        
        # Iterate over each element of ransomNote string 
        for e in ransomNote:
            
            if ransomNote.count(e) > magazine.count(e):
                
                return False
            
            elif e in magazine:
                
                c = c + 1
                
        if c == len(ransomNote):
                    
            return True
                
        else:
            
            return False
                
                
  # https://leetcode.com/problems/ransom-note/submissions/
