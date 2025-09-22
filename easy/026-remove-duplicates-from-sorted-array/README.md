# 26. Remove Duplicates from Sorted Array

## 📋 문제 정보

- **난이도**: Easy
- **링크**: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
- **카테고리**: Array, Two Pointers

## 📝 문제 설명

정렬된 배열 `nums`에서 중복을 in-place로 제거하여 각 원소가 한 번만 나타나도록 하세요. 제거 후의 길이 `k`를 반환합니다. `nums[0..k-1]`만 유효하며, 그 뒤 값은 무엇이든 상관없습니다.

### 예시

```
Input: nums = [0,0,1,1,1,2,2,3]
Output: k = 4, nums = [0,1,2,3,_,_,_,_]
```

## 💡 접근 방법

### 방법: 동일 방향 두 포인터 (write/read)

**핵심 아이디어:**
- 정렬 배열이므로 새로운 값이 나타날 때만 앞쪽에 덮어쓰기
- `write`는 다음 유니크 값이 들어갈 위치, `read`는 순회 인덱스

**알고리즘 단계:**
1. `write = 1`로 시작 (첫 값은 항상 유지)
2. `read`를 1부터 끝까지 순회
3. `nums[read] != nums[write-1]`이면 `nums[write] = nums[read]`, `write += 1`

**시간 복잡도**: O(n)  
**공간 복잡도**: O(1)

## 🔍 코드 구현

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1
        return write
```

## 📚 배운 점

- in-place 덮어쓰기를 위한 불변식: `nums[0..write-1]`는 항상 중복 없음
- 첫 원소 고정 후 `read=1`부터 시작하면 예외 분기 제거 가능

---

**해결 날짜**: 2025-09-22  
**소요 시간**: 15분  
**재시도 횟수**: 0회


