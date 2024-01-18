def solution(data):
  stack = []
  result = ""
  for i in data:
    # operand
    if i.isalpha():
      result += i
    # operator
    else:
      if i == "(":
        stack.append(i)
      elif i == ")":
        while stack and stack[-1] != "(":
          result += stack.pop()
        if stack[-1] == "(":
          stack.pop()
      elif stack and (stack[-1] == "*" or stack[-1] == "/"):
        if (i == "*" or i == "/"):
          result += stack.pop()
        else:
          while stack and stack[-1] != "(":
            result += stack.pop()
        stack.append(i)
      elif stack and (i == "+" or i == "-") and (stack[-1] == "+" or stack[-1] == "-"):
        result += stack.pop()
        stack.append(i)
      else:
        stack.append(i)
  while stack:
    result += stack.pop()

  return result

data = list(input())
print(solution(data))
