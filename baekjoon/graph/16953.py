def first(input):
  return input * 2


def second(input):
  return input * 10 + 1


a, b = map(int, input().split())

## bfs
import collections

queue = collections.deque()
queue.append((a, 1))

while queue:
  val, count = queue.popleft()
  if val == b:
    print(count)
    exit()
  elif val > b:
    continue
  count += 1
  queue.append((first(val), count))
  queue.append((second(val), count))
  

print(-1)