class Solution:
    def countElements(self, nums: List[int], k: int) -> int:

        n = len(nums)

        if k == 0:
            return n

        nums.sort()

        ans = 0

        for i in range(n - k):
            if nums[i] < nums[n - k]:
                ans += 1

        return ans      