
# 내 풀이
# n, m = map(int, input().split())

# nums = list(map(int, input().split()))
# nums.sort()

# res = []
# result_idxs = []

# def bfs(remain):
#   if len(res) == m:
#     result_idxs.append(res[:])
#     return

#   for _ in range(len(remain)):
#     val = remain.pop(0)
#     res.append(val)
#     bfs(remain)
#     remain.append(val)
#     res.pop()

# bfs([i for i in range(0, n)])

# result_idxs.sort()
# for idxs in result_idxs:
#   result = [nums[i] for i in idxs]
#   print(' '.join(map(str, result)))

# 간단한 풀이...
  
N, M = map(int, input().split())
numbers = [int(x) for x in input().split()]

numbers.sort()

def backtracking(depth):
    if depth == M:
        print(' '.join(map(str,box)))
        return

    for i in range(N):
        if numbers[i] in box:
            continue
        box.append(numbers[i])
        backtracking(depth + 1)
        box.pop()

box = []
backtracking(0)
