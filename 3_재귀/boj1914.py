# 문제: 하노이 탑 (실버 1)
# 수학적 귀납법 접근

# 기둥 구조:[시작 기둥] [보조 기둥] [타겟 기둥]
# base case: 원판1을 시작 기둥 -> 타겟 기둥 이동 (탈출 조건)
# general case: 
# - 가정: n개의 원판 그룹을 옮기는 법을 알고 있다. 
# - 재귀: 그렇다면 n+1개의 원판 그룹을 옮기는 법은 다음과 같다.
# 1. 위의 n개의 원판 그룹을 [시작 -> 보조] 기둥 이동
# 2. 아래 가장 큰 원판(n+1번째 원판)을 직접 [시작 -> 타겟] 기둥 이동
# 3. 1번에서 옮긴 n개의 원판 그룹을 [보조 -> 타겟] 기둥 이동

# 위 내용이 성립하면, n개의 원판 그룹에 대하여 하노이의 탑은 성립한다. 

# -------------------------------------------

# 원판은 start 자리(2번째 인자) -> target 자리(4번째 인자)로 감. 인자 위치 변화에 따른 헷갈림에 주의
# 원판 이동 행위는 print()로 구현
def hanoi(n, start, sub, target, count):
    # base case
    if n == 1:
        print(start, target)
        return count
    # general case
    else:
        # 1. 위의 n-1개의 원판 그룹을 [시작 -> 보조] 기둥 이동
        hanoi(n-1, start, target, sub, count+1) # 보조 기둥이 타겟이 됨.
        # 2. 아래 가장 큰 원판(n+1번째 원판)을 직접 [시작 -> 타겟] 기둥 이동
        print(start, target)
        # 3. 1번에서 옮긴 n-1개의 원판 그룹을 [보조 -> 타겟] 기둥 이동
        hanoi(n-1, sub, start, target, count+1)



N = int(input())

print(2**(N)-1)
if N <= 20:
    hanoi(N, 1, 2, 3, 1)    
    


