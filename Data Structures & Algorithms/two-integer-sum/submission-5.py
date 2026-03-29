class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i
        for i, a in enumerate(nums):
            comp = target - a
            if comp in hash and hash[comp] != i:
                return [i, hash[comp]]
        