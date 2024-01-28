# DP

N = int(input())
array = list(map(int, input().split()))
dict = {}

for val in array:
  # 이미 저장된 val보다 작은 값 중에 count가 가장 큰 값 찾기 
  max = 0
  for compare in dict:
    if val > compare and dict[compare] > max:
      max = dict[compare]

  # 현재 값의 count 저장
  if max != 0:
    dict[val] = max + 1
  else:
    if val in dict:
      dict[val] = dict[val]
    else:
      dict[val] = 1

# 최대값 찾기
max = 0
for i in dict.values():
  if i > max:
    max = i
print(max)

