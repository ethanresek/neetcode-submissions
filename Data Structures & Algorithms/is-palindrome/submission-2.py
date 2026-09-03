class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned += c

        front = 0
        back = len(cleaned) - 1

        while front < back:
            
            if cleaned[front].lower() != cleaned[back].lower():
                return False
            front += 1
            back -= 1
        
        return True