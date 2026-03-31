class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxtoright = float('inf')
        ans = []
        for i in range(len(arr)-1):
            maxtoright = max(arr[i+1:])
            ans.append(maxtoright)
        print(ans)
        ans.append(-1)
        return ans
            

