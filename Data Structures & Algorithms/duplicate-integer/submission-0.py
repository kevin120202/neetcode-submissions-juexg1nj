class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        for num in nums:
            dups[num] = dups.get(num, 0) + 1
            if dups[num] > 1:
                return True
        return False