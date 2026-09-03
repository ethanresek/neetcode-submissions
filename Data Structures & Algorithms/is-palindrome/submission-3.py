class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = s.lower()

        front = 0
        back = len(cleaned) - 1

        while front < back:
            if not cleaned[front].isalnum():
                front += 1
            elif not cleaned[back].isalnum():
                back -= 1
            else:            
                if cleaned[front].lower() != cleaned[back].lower():
                    return False
                front += 1
                back -= 1
        
        return True