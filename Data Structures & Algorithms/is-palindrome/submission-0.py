class Solution:
    def isPalindrome(self, s: str) -> bool:
        spaceless = "".join([char for char in s if char.isalnum()]).lower()
        if spaceless == spaceless[::-1]:
            return True
        else:
            return False
        