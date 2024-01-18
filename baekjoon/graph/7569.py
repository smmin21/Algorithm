import collections
def main():
  m, n, h = map(int, input().split())
  box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
  tomato = collections.deque()
  un_tomato = []
  result = 0
  
  # Initialize
  for a in range(h):
    for b in range(n):
      for c in range(m):
        if box[a][b][c] == 1:
          tomato.append((a, b, c))
        elif box[a][b][c] == 0:
          un_tomato.append((a, b, c))

  # BFS
  un_len = len(un_tomato)
  while un_len != 0:
    iter_num = len(tomato)
    
    # If there is no tomato to spread
    if iter_num == 0:
      print(-1)
      break
      
    # Spread tomato
    for _ in range(iter_num):
      x, y, z = tomato.popleft()
      dir = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
      for d_x, d_y, d_z in dir:
        nx, ny, nz = x + d_x, y + d_y, z + d_z
        if (0 <= nx < h and 0 <= ny < n and 0 <= nz < m) and box[nx][ny][nz] == 0:
            box[nx][ny][nz] = 1
            tomato.append((nx, ny, nz))
            un_len -= 1
    result += 1
  
  if un_len == 0:
    print(result)

main()
  