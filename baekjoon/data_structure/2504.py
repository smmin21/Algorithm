input = list(map(str, input()))
stack = []
scores = []
result = 0
level = 0

closed = [')', ']']
pair = {'(': ')', '[': ']'}
# 곱셈 1 덧셈 0

for i in input:
  if i in pair:
    level += 1
    stack.append(i)
    if i == '(':
      scores.append([2, level])
    else:
      scores.append([3, level])
  else:
    if i == ')':
      if stack and stack[-1] == '(':
        stack.pop()
        level -= 1
      else:
        print(0)
        exit()
    elif i == ']':
      if stack and stack[-1] == '[':
        stack.pop()
        level -= 1
      else:
        print(0)
        exit()
if stack:
  print(0)
  exit()

if not scores:
  print(0)
  exit()


# print(scores)
##############################################
op = []
post_calc = '' + str(scores[0][0])

if len(scores) > 1:
  for i in range(len(scores) - 1):
    if scores[i][1] < scores[i + 1][1]:
      op.append(['*', scores[i + 1][1]])
      post_calc += str(scores[i + 1][0])
    elif scores[i][1] == scores[i + 1][1]:
      op.append(['+', scores[i + 1][1]])
      post_calc += str(scores[i + 1][0])
    else:
      while op and (op[-1][1] > scores[i + 1][1]):
        post_calc += str(op.pop()[0])
      post_calc += str(scores[i + 1][0])
      op.append(['+', scores[i + 1][1]])
  while op:
    post_calc += str(op.pop()[0])

# print(post_calc)
################################################

op_check = ['+', '*']
last_stack = []
a1, a2 = 0, 0
for l in range(len(post_calc)):
  if post_calc[l] not in op_check:
    last_stack.append(int(post_calc[l]))
  elif post_calc[l] == '+':
    a1 = last_stack.pop()
    a2 = last_stack.pop()
    last_stack.append(a1 + a2)
  elif post_calc[l] == '*':
    a1 = last_stack.pop()
    a2 = last_stack.pop()
    last_stack.append(a1 * a2)
print(last_stack[0])
