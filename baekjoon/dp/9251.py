## 힌트 참고함!
## 다시 풀어보기!

str1 = input()
str2 = input()

result = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i, w1 in enumerate(str1):
  for j, w2 in enumerate(str2):
    if w1 == w2:
      result[i + 1][j + 1] = result[i][j] + 1
    else:
      result[i + 1][j + 1] = max(result[i][j + 1], result[i + 1][j])


print(result[-1][-1])