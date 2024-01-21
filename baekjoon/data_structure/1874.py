n = int(input())
list = [int(input()) for _ in range(n)]
# list = list(map(int, input().split()))

max = list[0]
answer = []
real = []
for i in range(1, max + 1):
  answer.append('+')
  real.append(i)
answer.append('-')
real.pop()
error = 0

for i in range(len(list) - 1):
  now = list[i]
  next = list[i + 1]
  if now < next:
    if next > max:
      for j in range(max + 1, next + 1):
        answer.append('+')
        real.append(j)
      max = next
      answer.append('-')
      real.pop()
    else:
      print('NO')
      error = 1
      break
  else:
    if real and real[-1] == next:
      answer.append('-')
      real.pop()
    else:
      print('NO')
      error = 1
      break

if error == 0:
  print('\n'.join(answer))
