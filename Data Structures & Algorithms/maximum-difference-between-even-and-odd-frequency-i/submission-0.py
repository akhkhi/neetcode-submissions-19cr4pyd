class Solution:
    def maxDifference(self, s: str) -> int:
        s_freq = {}

        for i in range(len(s)):
            s_freq[s[i]] = 1 + s_freq.get(s[i], 0)
        print(s_freq)
        maxodd = float('-inf')
        mineven = float('inf')
        for i in s_freq.values():
            if i % 2 != 0 and i > maxodd:
                maxodd = i
            if i % 2 == 0 and i < mineven:
                mineven = i
            
            
        return maxodd - mineven
        