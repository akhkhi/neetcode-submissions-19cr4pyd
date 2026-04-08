class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = 1 + nums_dict.get(nums[i], 0)

        for i in nums_dict:
            if nums_dict[i] > len(nums) / 2:
                return i

        