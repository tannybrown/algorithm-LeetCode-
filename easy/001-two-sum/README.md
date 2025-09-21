# 1. Two Sum

## 📋 문제 정보

- **난이도**: Easy
- **링크**: https://leetcode.com/problems/two-sum/
- **카테고리**: Array, Hash Table

## 📝 문제 설명

정수 배열 `nums`와 정수 `target`이 주어졌을 때, `target`과 같은 두 수의 인덱스를 반환하세요.

각 입력에 대해 정확히 하나의 해답이 있다고 가정할 수 있으며, 같은 원소를 두 번 사용할 수 없습니다.

### 예시

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9이므로 [0, 1]을 반환합니다.
```

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## 💡 접근 방법

### 방법 1: Hash Map (One-pass)

**핵심 아이디어:**
- 배열을 순회하면서 각 원소에 대해 `target - 현재원소`가 이미 해시맵에 있는지 확인
- 있다면 현재 인덱스와 해시맵에 저장된 인덱스를 반환
- 없다면 현재 원소와 인덱스를 해시맵에 저장

**알고리즘 단계:**
1. 빈 해시맵 `elements = {}` 생성
2. 배열을 순회하면서:
   - `rest_num = target - num` 계산
   - `rest_num`이 해시맵에 있으면 `[현재인덱스, 저장된인덱스]` 반환
   - 없으면 `elements[num] = i`로 저장
3. 순회 완료

**시간 복잡도**: O(n) - 배열을 한 번만 순회  
**공간 복잡도**: O(n) - 최악의 경우 모든 원소를 해시맵에 저장

### 방법 2: Brute Force (참고용)

이중 반복문으로 모든 조합을 확인하는 방법도 있지만, O(n²) 시간 복잡도로 비효율적입니다.

## 🔍 코드 구현

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {}
        for i, num in enumerate(nums):
            rest_num = target - num
            if rest_num in elements:
                return [i, elements[rest_num]]
            elements[num] = i
```

## 🧪 테스트 결과

| 테스트 케이스 | 입력 | 출력 | 결과 |
|-------------|------|------|------|
| 1 | nums=[2,7,11,15], target=9 | [0,1] | ✅ |
| 2 | nums=[3,2,4], target=6 | [1,2] | ✅ |
| 3 | nums=[3,3], target=6 | [0,1] | ✅ |

## 📚 배운 점

- **Hash Map의 활용**: O(1) 조회 시간을 활용한 최적화
- **One-pass 알고리즘**: 한 번의 순회로 문제 해결 가능
- **공간-시간 트레이드오프**: 추가 공간을 사용해 시간 복잡도 개선
- **인덱스 관리**: 값이 아닌 인덱스를 반환하는 문제의 특성

## 🔗 관련 문제

- 15. 3Sum
- 18. 4Sum
- 167. Two Sum II - Input array is sorted
- 653. Two Sum IV - BST

---

**해결 날짜**: 2025-09-21  
**소요 시간**: 첫 번째 시도에서 해결  
**재시도 횟수**: 0회
