class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #iterate through the loop than check if num is not equal to val if it isnt increment k by one
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k