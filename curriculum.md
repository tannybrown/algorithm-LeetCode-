# 🎯 구글 면접 대비 알고리즘 커리큘럼

**목표**: 학부 지식 복습 + LeetCode 마스터 → 구글 면접 합격

## 📅 4주 완성 로드맵

### **Week 1: 기초 자료구조 복습 + Array/String 패턴**
**목표**: 기본기 다지기 + Hash Map/Two Pointers 마스터

#### Day 1 (내일) - Array + Hash Map 기초
**복습할 개념**:
- 배열의 시간복잡도 (접근: O(1), 삽입/삭제: O(n))
- Hash Map/Set 개념 (O(1) 평균 조회)

**풀 문제들**:
1. **217. Contains Duplicate** (Hash Set 기초)
2. **242. Valid Anagram** (Hash Map counting)
3. **1. Two Sum** ✅ (이미 완료!)

**학습 포인트**: Hash 자료구조가 언제 유용한지 체감

#### Day 2 - Two Pointers 패턴
**복습할 개념**:
- 정렬 알고리즘 복습 (시간복잡도)
- Two Pointers 기본 원리

**풀 문제들**:
1. **125. Valid Palindrome** (기본 Two Pointers)
2. **167. Two Sum II** (정렬된 배열)
3. **15. 3Sum** (도전 문제)

#### Day 3-4 - String 처리
**복습할 개념**:
- 문자열 조작 시간복잡도
- ASCII/Unicode 기본

**풀 문제들**:
1. **20. Valid Parentheses** (Stack 개념 도입)
2. **3. Longest Substring Without Repeating** (Sliding Window)
3. **49. Group Anagrams**

#### Day 5-7 - 복습 및 패턴 정리
- 이번 주 문제들 다시 풀어보기
- 패턴별 노트 정리

---

### **Week 2: 연결리스트 + 스택/큐**
**목표**: 포인터 조작 + 기본 자료구조 마스터

#### Day 8-10 - 연결리스트
**복습할 개념**:
- 연결리스트 vs 배열 차이점
- 포인터 조작 기본기

**풀 문제들**:
1. **206. Reverse Linked List**
2. **141. Linked List Cycle** (Fast & Slow Pointers)
3. **21. Merge Two Sorted Lists**

#### Day 11-14 - 스택/큐 + 기본 트리
**복습할 개념**:
- Stack/Queue LIFO/FIFO 개념
- 이진트리 기본 구조

**풀 문제들**:
1. **155. Min Stack**
2. **232. Implement Queue using Stacks**
3. **104. Maximum Depth of Binary Tree** (DFS 기초)
4. **226. Invert Binary Tree**

---

### **Week 3: 트리/그래프 + 재귀**
**목표**: DFS/BFS 마스터

#### Day 15-17 - 이진트리 DFS
**복습할 개념**:
- 전위/중위/후위 순회
- 재귀 vs 반복 구현

**풀 문제들**:
1. **144. Binary Tree Preorder Traversal**
2. **94. Binary Tree Inorder Traversal**
3. **543. Diameter of Binary Tree**

#### Day 18-21 - BFS + 그래프 기초
**복습할 개념**:
- BFS vs DFS 차이점
- 그래프 표현 방법 (인접리스트/행렬)

**풀 문제들**:
1. **102. Binary Tree Level Order Traversal** (BFS)
2. **200. Number of Islands** (그래프 DFS)
3. **133. Clone Graph**

---

### **Week 4: 동적계획법 + 백트래킹**
**목표**: 최적화 문제 해결

#### Day 22-24 - DP 기초
**복습할 개념**:
- 메모이제이션 vs 테이블
- 최적 부분구조

**풀 문제들**:
1. **70. Climbing Stairs** (피보나치 변형)
2. **198. House Robber**
3. **121. Best Time to Buy and Sell Stock**

#### Day 25-28 - 백트래킹 + 종합 복습
**복습할 개념**:
- 백트래킹 vs DFS
- 가지치기 최적화

**풀 문제들**:
1. **46. Permutations**
2. **78. Subsets**
3. **종합 복습**: 이전 문제들 다시 풀기

---

## 🗓️ 일일 학습 루틴 (2-3시간)

### 📚 **학습 순서** (매일)
1. **개념 복습** (30분)
   - 해당 자료구조/알고리즘 이론 정리
   - 시간/공간 복잡도 분석

2. **문제 해결** (90분)
   - 첫 번째 문제: 15분 고민 → 힌트 보고 해결
   - 두 번째 문제: 20분 고민 → 직접 해결 시도
   - 세 번째 문제: 도전 문제 (못 풀어도 OK)

3. **정리 및 복습** (30분)
   - README.md 작성
   - 패턴 노트 정리
   - GitHub 커밋

### 📝 **주간 복습**
- **금요일**: 이번 주 문제들 다시 풀어보기
- **일요일**: 다음 주 개념 미리 학습

---

## 🎯 **내일(Day 1) 구체적 계획**

### 🌅 **아침 준비** (30분)
```bash
# 새 폴더 생성
mkdir easy/217-contains-duplicate
mkdir easy/242-valid-anagram

# 개념 복습
# - 배열 vs Hash Set 성능 차이
# - Hash 충돌 처리 방법
```

### 🔥 **문제 해결** (90분)

#### 1. **217. Contains Duplicate** (30분)
- **개념**: Hash Set 기본 사용법
- **패턴**: 중복 검사
- **예상 난이도**: ⭐⭐☆☆☆

#### 2. **242. Valid Anagram** (30분)
- **개념**: Hash Map으로 개수 세기
- **패턴**: 문자 빈도 비교
- **예상 난이도**: ⭐⭐☆☆☆

#### 3. **49. Group Anagrams** (30분) - 도전!
- **개념**: Hash Map + 정렬
- **패턴**: 그룹핑
- **예상 난이도**: ⭐⭐⭐☆☆

### 📚 **정리** (30분)
- 각 문제별 README.md 작성
- Hash 자료구조 사용 패턴 정리
- GitHub 커밋

---

## 💡 **학습 팁**

### 🧠 **기억 복구 전략**
1. **개념부터**: 문제 풀기 전에 자료구조 개념부터
2. **시각화**: 그림 그리면서 이해하기
3. **반복**: 같은 패턴 문제 여러 개 풀기

### 🎯 **면접 준비**
- 매 문제마다 **말로 설명하는 연습**
- 시간/공간 복잡도 **반드시** 분석
- 다른 접근법도 **한 번씩** 생각해보기

### 📈 **진도 관리**
- 못 푼 문제는 **표시해두고** 나중에 다시
- **완벽보다는 꾸준함**이 중요
- 주 단위로 **패턴 정리** 필수

---

이 커리큘럼 어떠세요? 너무 빡빡하거나 느슨한 부분이 있다면 조정해드릴게요! 🚀
