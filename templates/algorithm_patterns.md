# 🧩 알고리즘 패턴 정리

구글 면접 및 LeetCode에서 자주 나오는 핵심 알고리즘 패턴들을 정리한 가이드입니다.

## 📋 목차

1. [Two Pointers (투 포인터)](#two-pointers)
2. [Sliding Window (슬라이딩 윈도우)](#sliding-window)
3. [Hash Map/Set](#hash-mapset)
4. [Fast & Slow Pointers](#fast--slow-pointers)
5. [Merge Intervals](#merge-intervals)
6. [Cyclic Sort](#cyclic-sort)
7. [Tree DFS](#tree-dfs)
8. [Tree BFS](#tree-bfs)
9. [Dynamic Programming](#dynamic-programming)
10. [Backtracking](#backtracking)

---

## Two Pointers

**언제 사용**: 정렬된 배열이나 연결리스트에서 특정 조건을 만족하는 쌍을 찾을 때

### 패턴 구조
```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []
```

### 대표 문제
- 1. Two Sum (Hash Map 버전도 있음)
- 15. 3Sum
- 167. Two Sum II - Input array is sorted
- 344. Reverse String

### 시간/공간 복잡도
- 시간: O(n)
- 공간: O(1)

---

## Sliding Window

**언제 사용**: 연속된 부분 배열/문자열에서 최대/최소값을 찾을 때

### 패턴 구조
```python
def sliding_window(arr, k):
    window_start = 0
    max_sum = 0
    window_sum = 0
    
    # 첫 번째 윈도우
    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # 오른쪽 확장
        
        # 윈도우 크기가 k에 도달하면
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]  # 왼쪽 축소
            window_start += 1
    
    return max_sum
```

### 대표 문제
- 3. Longest Substring Without Repeating Characters
- 76. Minimum Window Substring
- 209. Minimum Size Subarray Sum
- 424. Longest Repeating Character Replacement

### 시간/공간 복잡도
- 시간: O(n)
- 공간: O(1) ~ O(k)

---

## Hash Map/Set

**언제 사용**: 빠른 조회가 필요하거나 중복 확인이 필요할 때

### 패턴 구조
```python
def hash_pattern(arr):
    seen = set()  # 또는 {}
    
    for num in arr:
        if num in seen:
            return True  # 중복 발견
        seen.add(num)
    
    return False
```

### 변형 패턴들
```python
# 개수 세기
from collections import Counter
count_map = Counter(arr)

# 값 -> 인덱스 매핑
num_to_index = {num: i for i, num in enumerate(arr)}

# 조건부 저장
complement_map = {}
for i, num in enumerate(arr):
    complement = target - num
    if complement in complement_map:
        return [complement_map[complement], i]
    complement_map[num] = i
```

### 대표 문제
- 1. Two Sum ✅
- 217. Contains Duplicate
- 242. Valid Anagram
- 49. Group Anagrams

---

## Fast & Slow Pointers

**언제 사용**: 연결리스트에서 사이클 검출이나 중점 찾기

### 패턴 구조
```python
def has_cycle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False
```

### 대표 문제
- 141. Linked List Cycle
- 142. Linked List Cycle II
- 876. Middle of the Linked List
- 202. Happy Number

---

## Tree DFS

**언제 사용**: 트리의 모든 경로를 탐색하거나 깊이 우선으로 처리할 때

### 패턴 구조
```python
def dfs_recursive(root):
    if not root:
        return
    
    # 전위 처리
    process(root.val)
    
    dfs_recursive(root.left)
    dfs_recursive(root.right)

def dfs_iterative(root):
    if not root:
        return
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        process(node.val)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
```

### 대표 문제
- 104. Maximum Depth of Binary Tree
- 112. Path Sum
- 226. Invert Binary Tree
- 543. Diameter of Binary Tree

---

## Dynamic Programming

**언제 사용**: 최적 부분 구조와 중복 부분 문제가 있을 때

### 패턴 구조
```python
# Top-down (메모이제이션)
def dp_memo(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = dp_memo(n-1, memo) + dp_memo(n-2, memo)
    return memo[n]

# Bottom-up (테이블)
def dp_table(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

### 대표 문제
- 70. Climbing Stairs
- 198. House Robber
- 121. Best Time to Buy and Sell Stock
- 322. Coin Change

---

## 🎯 패턴 선택 가이드

| 문제 유형 | 추천 패턴 | 키워드 |
|----------|----------|--------|
| 정렬된 배열에서 쌍 찾기 | Two Pointers | "sorted", "pair", "target sum" |
| 연속 부분배열 최적화 | Sliding Window | "subarray", "substring", "consecutive" |
| 빠른 조회/중복 확인 | Hash Map/Set | "duplicate", "count", "frequency" |
| 연결리스트 사이클 | Fast & Slow | "cycle", "middle", "linked list" |
| 트리 탐색 | DFS/BFS | "tree", "path", "depth" |
| 최적화 문제 | Dynamic Programming | "maximum", "minimum", "count ways" |

---

## 💡 패턴 마스터 팁

1. **패턴 인식**: 문제를 읽자마자 어떤 패턴인지 파악하는 연습
2. **템플릿 암기**: 각 패턴의 기본 구조를 외우기
3. **변형 연습**: 같은 패턴의 다양한 문제로 응용력 기르기
4. **복합 패턴**: 여러 패턴을 조합한 문제 해결 능력

**구글 면접 팁**: 패턴을 말로 설명할 수 있어야 합니다!
- "이 문제는 Two Pointers 패턴으로 해결할 수 있습니다..."
- "Sliding Window를 사용하면 O(n) 시간에 해결 가능합니다..."
