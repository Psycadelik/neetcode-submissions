class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for number in nums:
            counts[number] = counts.get(number, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for number, frequency in counts.items():
            buckets[frequency].append(number)

        result = []

        for frequency in range(len(buckets) - 1, 0, -1):
            for number in buckets[frequency]:
                result.append(number)

                if len(result) == k:
                    return result
        return result