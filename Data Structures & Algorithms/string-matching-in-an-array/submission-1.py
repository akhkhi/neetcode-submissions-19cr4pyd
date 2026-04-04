class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sub = []
        for s in words:
            for w in words:
                if s in w and s != w:
                    if s not in sub:
                        sub.append(s)
        return sub