class Solution:
    def maxSubArray(self, nums):

        def solve(l, r):
            if l == r:
                return nums[l]

            mid = (l + r) // 2

            left = solve(l, mid)
            right = solve(mid + 1, r)

            s = 0
            leftMax = float('-inf')
            for i in range(mid, l - 1, -1):
                s += nums[i]
                leftMax = max(leftMax, s)

            s = 0
            rightMax = float('-inf')
            for i in range(mid + 1, r + 1):
                s += nums[i]
                rightMax = max(rightMax, s)

            return max(left, right, leftMax + rightMax)

        return solve(0, len(nums) - 1)