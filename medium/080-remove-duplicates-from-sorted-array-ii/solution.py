"""
LeetCode Problem: 80. Remove Duplicates from Sorted Array II
난이도: Medium
링크: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

시간 복잡도: O(n)
공간 복잡도: O(1)
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        각 원소가 최대 2번까지 허용되도록 in-place로 압축합니다.
        write 포인터 앞의 구간은 항상 "각 값이 최대 2회"를 만족하는 불변식을 유지합니다.
        """
        if len(nums) <= 2:
            return len(nums)

        write = 2
        for read in range(2, len(nums)):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1
        return write


if __name__ == "__main__":
    s = Solution()
    arr = [0,0,1,1,1,1,2,3,3]
    k = s.removeDuplicates(arr)
    print(k, arr[:k])  # Expected: 7 [0,0,1,1,2,3,3]


