class Solution:
    def removeElement(self, nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val: #if number isnt equal to the value keep it 
                nums[k] = nums[i]
                k += 1

        return k