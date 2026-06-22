class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        output = False

        seen = []

        for num in nums:
            if num in seen:
                output = True
            seen.append(num)

        return output