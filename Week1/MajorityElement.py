class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(n) time complexity
        length = len(nums)
        occurs = dict()
        for num in nums:
            if num in occurs.keys():
                occurs[num] += 1
            else:
                occurs[num] = 1
            if occurs[num] >= length/2:
                return num
        