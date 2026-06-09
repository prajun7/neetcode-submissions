class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumMap = {}
        for i in range(len(nums)):
            anotherNum = target - nums[i]
            if anotherNum in twoSumMap:
                return [twoSumMap[anotherNum], i]
            twoSumMap[nums[i]] = i