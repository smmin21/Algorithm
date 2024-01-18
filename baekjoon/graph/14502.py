import collections
import copy

n, m = map(int, input().split())
result = 0
graph = []
queue = collections.deque()  # 바이러스 위치 저장

# Initialize
for i in range(n):
  row = list(map(int, input().split()))
  graph.append(row)
  for j in range(m):
    if row[j] == 2:
      queue.append((i, j))

# Make 3 walls (DFS)
def wall(count):
  global result
  if count == 3:
    tmp = bfs(copy.deepcopy(graph), copy.deepcopy(queue))
    result = max(tmp, result)
    return
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        wall(count + 1)
        graph[i][j] = 0

# Spread virus (BFS)
def bfs(board, que):
  while que:
    x, y = que.popleft()
    dir_x = [-1, 0, 1, 0]
    dir_y = [0, 1, 0, -1]
    for i in range(4):
      nx, ny = x + dir_x[i], y + dir_y[i]
      if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
        board[nx][ny] = 2
        que.append((nx, ny))

  # Count zero
  zero_count = 0
  for i in range(n):
    for j in range(m):
      if board[i][j] == 0:
        zero_count += 1
  return zero_count

wall(0)
print(result)
