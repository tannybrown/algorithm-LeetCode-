"""
LeetCode Problem: 1. Two Sum
난이도: Easy
링크: https://leetcode.com/problems/two-sum/

시간 복잡도: O(n)
공간 복잡도: O(n)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        접근 방법:
        1. Hash Map을 사용하여 원패스로 해결
        2. 각 원소에 대해 target - num이 이미 존재하는지 확인
        3. 존재하면 현재 인덱스와 저장된 인덱스 반환
        4. 존재하지 않으면 현재 원소와 인덱스를 해시맵에 저장
        
        Args:
            nums: 정수 배열
            target: 목표 합계
            
        Returns:
            두 수의 인덱스를 담은 리스트
        """
        elements = {}  # {값: 인덱스} 매핑
        
        for i, num in enumerate(nums):
            rest_num = target - num
            if rest_num in elements:
                return [i, elements[rest_num]]
            elements[num] = i


# 테스트 케이스
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    result1 = solution.twoSum([2, 7, 11, 15], 9)
    print(f"Test 1: {result1}")  # Expected: [0, 1] 또는 [1, 0]
    
    # Test case 2  
    result2 = solution.twoSum([3, 2, 4], 6)
    print(f"Test 2: {result2}")  # Expected: [1, 2] 또는 [2, 1]
    
    # Test case 3
    result3 = solution.twoSum([3, 3], 6)
    print(f"Test 3: {result3}")  # Expected: [0, 1]
