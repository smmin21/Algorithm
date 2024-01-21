N = int(input())
pairs = [[] for _ in range(N + 1)]
result = [0] * (N + 1)
result[1] = 1

import sys

for _ in range(1, N):
  a, b = map(int, sys.stdin.readline().rstrip('\n').split(' '))
  pairs[a].append(b)
  pairs[b].append(a)

import collections

queue = collections.deque()
queue.append(1)
while queue:
  node = queue.popleft()
  for val in pairs[node]:
    if result[val] == 0:
      queue.append(val)
      result[val] = node

print('\n'.join(map(str, result[2:])))