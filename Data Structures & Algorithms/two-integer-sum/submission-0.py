class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, number in enumerate(nums):
            complement = target - number

            if complement in seen:
                return [seen[complement], idx]
            else:
                seen[number] = idx
        return []
