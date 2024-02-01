# 쉬운 DP 문제
# 20분 컷
# '현재' 위치에 포커스하여, 이전 위치의 값들 중 최소값을 더해주면 된다.

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

idx = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
for i in range(1, n):
  for j in range(3):
    costs[i][j] += min(costs[i-1][idx[j][0]], costs[i-1][idx[j][1]])
    
print(min(costs[-1]))