class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sub = set()
        for s in words:
            for w in words:
                if s in w and s != w:
                        sub.add(s)
        return list(sub)