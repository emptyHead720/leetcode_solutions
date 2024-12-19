class Solution(object):
    def removeDuplicates(self, nums):
        current_value = nums[0]
        last_index = 0
        for val in nums:
            if val != current_value:
                last_index += 1
                nums[last_index] = val
                current_value = val
        return last_index + 1
# why is the following solution not working on the website?
# nums = set(nums)
# nums = list(nums)
# print(nums)
# return len(nums)


def main():
    obj = Solution()
    s = obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    print(s)


if __name__=="__main__":
    main()
