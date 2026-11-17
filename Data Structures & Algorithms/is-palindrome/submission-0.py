class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Trim spaces and bring to lower case
        #Reverse the string
        #If reversed string == original string in trimmed and lower,then true
        formatted = ""
        for char in s:
            if char.isalnum():
                formatted += char.lower()
                
        reversed_s = ""
        for char in formatted:
            reversed_s = char+reversed_s

        if formatted == reversed_s:
            return True
        else:
            return False
