class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        occurrence = 0
        for i, num in enumerate(nums):
            if num == val:
                occurrence += 1
            else:
                nums[i-occurrence] = num
        print(nums)
        return len(nums) - occurrence

obj = Solution()
print(obj.removeElement([3, 2, 2, 3], 3))
