class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for right in range(len(nums)):
            left = len(nums)-1
            while left > right:
                summ = nums[right] + nums[left]
                if summ == target:
                    return [right, left]
                else:
                    left-=1


        