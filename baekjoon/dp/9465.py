T = int(input())
final = []

for _ in range(T):
  N = int(input())
  sticker = []
  sticker.append(list(map(int, input().split())))
  sticker.append(list(map(int, input().split())))

  result = [[], []]
  for i in range(N):
    # i - 2 번째 값에 접근하기 위해 i가 0, 1일 때는 따로 처리
    if i == 0:
      result[0].append(sticker[0][i])
      result[1].append(sticker[1][i])
    elif i == 1:
      result[0].append(sticker[0][i] + sticker[1][i - 1])
      result[1].append(sticker[1][i] + sticker[0][i - 1])
    # i - 2 번째 값 중 최대 or 가능한 i - 1 번째 값 중 최대
    else:
      max_0 = max(result[0][i - 2], result[1][i - 2], result[1][i - 1])
      result[0].append(max_0 + sticker[0][i])
      max_1 = max(result[0][i - 2], result[1][i - 2], result[0][i - 1])
      result[1].append(max_1 + sticker[1][i])
  final.append(max(result[0][N - 1], result[1][N - 1]))
      


print('\n'.join(map(str, final)))