




# Day 1 - 22 oct 2026 ( [Easy] 9. Palindrome Number ) ===========================================================================================
class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = str(x)[::-1]
        return True if str(x) == reverse else False


# ================================================================================================================================================

# Day 2 - 24 oct 2026 ( [Easy] 1. Two Sum ) ===========================================================================================
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in hash_map:
                return [hash_map[diff],i]

            hash_map[n] = i
            
def twoSum(nums, target):
    hash_map = {}

    for i, n in enumerate(nums):
        diff = target - n

        if diff in hash_map:
            return [hash_map[diff],i], hash_map

        hash_map[n] = i

# ================================================================================================================================================


