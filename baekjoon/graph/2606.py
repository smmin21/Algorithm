import collections
N = int(input())
iter = int(input())
graph = collections.defaultdict(list)

# 그래프 정보 저장
for _ in range(iter):
  n, m = map(int, input().split())
  graph[n].append(m)
  graph[m].append(n)

# BFS
queue = collections.deque()
queue.append(1)
result = set()
while queue:
  node = queue.popleft()
  result.add(node)
  for i in graph[node]:
    if i not in result:
      queue.append(i)
  
  
print(len(result) - 1)