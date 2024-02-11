# [풀이 1] 반복 구조로 구현하기
# n, m = map(int, input().split())

# result = [1] * (m - 1) + [0]

# while result != [n] * m:
#   for i in range(m - 1, -1, -1):
#     if result[i] + 1 <= n:
#       result[i] += 1
#       result[i + 1:] = [result[i]] * (m - i - 1)
#       break
#   print(' '.join(map(str, result)))

# [풀이 2] 재귀 구조로 구현하기 - 백트래킹
n, m = map(int, input().split())

res = []

def dfs(start):
  if len(res) == m:
    print(' '.join(map(str, res)))
    return

  for i in range(start, n + 1):
    res.append(i)
    dfs(i)
    res.pop()

dfs(1)