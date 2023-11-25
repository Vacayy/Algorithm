# 문제: 소형기관차
'''
반드시 limit개의 객차를 끄는 게 최선은 아님
    - ex) 35 40 50 10 100 45 60 인 경우 -> 기관차 한 대는 1개의 객차를 끌게 됨

DP 접근 (2차원 배열로 Tabulation 수행)
    - DP[i][j]: 최대 운송 손님 수 of 1) 기관차 i대를 운행할 때, 2) j번째 객차를 선택하고, 3) limit개의 객차를 넣었을 때
    - S[x] : x번째 객차까지의 모든 손님 수를 더한 배열
        - S[x] 생성 이유: x번째 객차를 선택했을 때 S[x] - S[x - limit]를 통해 기관차가 끌 수 있는 손님 수를 바로 알 수 있기 때문

점화식:
    DP[i][j] = max(i-1번째 객차까지의 결과, i번째 객차 고르고 j-1 번째 기관차에서 그 이전 객차들 고른 경우)
             = max(DP[i][j-1], DP[i-1][j-limit] + S[j] - S[j-limit])
'''
import sys
input = sys.stdin.readline

N = int(input())
train = list(map(int, input().split()))
limit = int(input())

S = [0]
value = 0
for a in train:
    value += a
    S.append(value)

# 테이블 생성
dp = [[0] * (N+1) for i in range(4)]

for i in range(1, 4):
    for j in range(i*limit, N+1): # i*limit 부터 시작하는 이유: 그 이전 객차들은 모두 선택되었을 것이므로
        if i == 1:
            dp[i][j] = max(dp[i][j-1], S[j] - S[j-limit])
        
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-limit] + S[j] - S[j-limit])

for i in dp:
    print(i)

print(dp[3][N]) 

