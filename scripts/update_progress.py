#!/usr/bin/env python3
"""
진행 상황을 자동으로 업데이트하는 스크립트
사용법: python scripts/update_progress.py
"""

import os
import json
from datetime import datetime
from pathlib import Path

def count_solved_problems():
    """해결된 문제 개수를 세는 함수"""
    base_path = Path(__file__).parent.parent
    
    counts = {"easy": 0, "medium": 0, "hard": 0}
    
    for difficulty in ["easy", "medium", "hard"]:
        difficulty_path = base_path / difficulty
        if difficulty_path.exists():
            # solution.py 파일이 있는 폴더 개수를 센다
            for problem_dir in difficulty_path.iterdir():
                if problem_dir.is_dir():
                    solution_file = problem_dir / "solution.py"
                    if solution_file.exists():
                        # 파일이 템플릿이 아닌 실제 구현인지 확인
                        with open(solution_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                            if "pass" not in content or len(content.split('\n')) > 30:
                                counts[difficulty] += 1
    
    return counts

def update_readme_stats(counts):
    """메인 README의 통계를 업데이트"""
    readme_path = Path(__file__).parent.parent / "README.md"
    
    if not readme_path.exists():
        return
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 진행 상황 테이블 업데이트
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if "| Easy   |" in line:
            lines[i] = f"| Easy   | {counts['easy']}             | TBD       | {counts['easy']}%     |"
        elif "| Medium |" in line:
            lines[i] = f"| Medium | {counts['medium']}             | TBD       | {counts['medium']}%     |"
        elif "| Hard   |" in line:
            lines[i] = f"| Hard   | {counts['hard']}             | TBD       | {counts['hard']}%     |"
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def main():
    print("📊 진행 상황을 업데이트하는 중...")
    
    # 해결된 문제 개수 계산
    counts = count_solved_problems()
    total = sum(counts.values())
    
    print(f"✅ 해결된 문제 개수:")
    print(f"   Easy: {counts['easy']}개")
    print(f"   Medium: {counts['medium']}개") 
    print(f"   Hard: {counts['hard']}개")
    print(f"   총합: {total}개")
    
    # README 업데이트
    update_readme_stats(counts)
    print("✅ README.md 업데이트 완료")
    
    # 진행 상황 파일 업데이트 (간단한 버전)
    progress_path = Path(__file__).parent.parent / "progress.md"
    if progress_path.exists():
        print("✅ progress.md 파일을 수동으로 업데이트해주세요.")
    
    print("🎉 업데이트 완료!")

if __name__ == "__main__":
    main()
