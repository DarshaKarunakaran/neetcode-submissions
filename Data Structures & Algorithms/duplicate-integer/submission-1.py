class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        end = len(nums)-1
        start = 0
        nums.sort()
        while end > start:
            if nums[start] == nums[start + 1]:
                return True
            if nums[end] == nums[end - 1]:
                return True
            else:
                end-=1
                start+=1
        return False