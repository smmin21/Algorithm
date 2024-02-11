str = input()

word = 'quack'

result = [0]
count = 1
check = 0

for i in str:
  vs = []
  for j in result:
    if j < 5:
      vs.append(word[j])
    else:
      vs.append(0)

  if i in vs:
    result[vs.index(i)] += 1
  elif i == 'q':
    result.append(1)
    count += 1
    if 5 in result:
      count -= 1
      result[result.index(5)] = 10
  else:
    print(-1)
    exit()


for i in result:
  if i != 5 and i !=10:
    print(-1)
    exit()
print(count)
