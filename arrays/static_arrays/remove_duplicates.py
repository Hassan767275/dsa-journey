class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #create two pointers one that iterates thorugh the loop and the other that stores only unique elements
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k