n, m = map(int, input().split())
listen = []
see = []
result = []

for _ in range(n):
  listen.append(input())

for _ in range(m):
  see.append(input())

i, j = 0, 0
listen.sort()
see.sort()

while i != len(listen) and j != len(see):
  if listen[i] == see[j]:
    result.append(listen[i])
    i += 1
    j += 1
  elif listen[i] > see[j]:
    j += 1
  else:
    i += 1

result.sort()
print(len(result))
for r in result:
  print(r)