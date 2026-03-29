class Solution:
    def isalpha(self, c):
        return (ord('A')<= ord(c) <=ord('Z')or
                ord('a')<= ord(c) <= ord('z')or
                ord('0')<= ord(c) <= ord('9')) 
    def isPalindrome(self, s: str) -> bool:

        new = ''
        for a in s:
            if a != ' ' and self.isalpha(a):
                new = new + a
         

        l = 0
        r = len(new) - 1
        print(new)
        while r > l:
            if new[r].lower() == new[l].lower():
                r = r -1
                l = l + 1
            else:
                return False
        return True
    
