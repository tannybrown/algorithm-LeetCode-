"""
LeetCode Problem: 26. Remove Duplicates from Sorted Array
난이도: Easy
링크: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

시간 복잡도: O(n)
공간 복잡도: O(1)
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        접근 방법:
        1. 동일 방향 두 포인터(write/read) 사용
        2. 정렬 배열 특성을 이용해 직전에 쓴 값과 다를 때만 덮어쓰기
        3. write는 중복 제거 후 다음 값이 들어갈 위치를 가리킴

        Args:
            nums: 정렬된 정수 배열 (len >= 1)

        Returns:
            중복 제거 후의 길이 k (nums[0..k-1]가 유효 구간)
        """
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1
        return write


# 테스트 케이스
if __name__ == "__main__":
    solution = Solution()

    arr = [0, 0, 1, 1, 1, 2, 2, 3]
    k = solution.removeDuplicates(arr)
    print(k, arr[:k])  # Expected: 4 [0, 1, 2, 3]


