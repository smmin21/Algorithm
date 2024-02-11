# 힌트 많이 참고함..
# 재귀 연습 많이 하기!

values = []
import sys
sys.setrecursionlimit(10**6)

while True:
  try:
    values.append(int(input()))
  except:
    break


def build_tree(l, r):
  if l == r:
    return

  pivot = values[l]
  left, right, mid = l + 1, r, r
  for i in range(l + 1, r):
    if values[i] > pivot:
      mid = i
      break

  build_tree(left, mid)
  build_tree(mid, right)
  # 이렇게 바로 출력해도 후위 순회 순서로 출력 된다!
  print(pivot)


build_tree(0, len(values))
