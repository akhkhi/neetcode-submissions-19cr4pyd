class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s2 = s.split()
        print(s)
        return len(s2[len(s2)-1])
        