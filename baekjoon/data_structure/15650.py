n, m = map(int, input().split())
output = []

def dfs(i, len):
  if len == m:
    print(' '.join(map(str, output)))
    return

  if i <= n:
    output.append(i)
    dfs(i + 1, len + 1)
    output.pop()
    dfs(i + 1, len)


dfs(1, 0)