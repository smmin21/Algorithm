N = int(input())


class tree:

  def __init__(self, val) -> None:
    self.val = val
    self.left = None
    self.right = None

  def set(self, left, right):
    self.left = left
    self.right = right

## Get tree input
root = tree(None)
dict = {}
for i in range(N):
  x, y, z = map(str, input().split())
  if i == 0:
    root, left, right = tree(x), tree(y), tree(z)
    dict[y], dict[z] = left, right
    root.set(left, right)
  else:
    node, left, right = dict[x], tree(y), tree(z)
    dict[y], dict[z] = left, right
    node.set(left, right)

## 1. pre-order
pre_order = ''
def pre_order_traversal(node):
  global pre_order
  if not node:
    return 
    
  if node.val != '.':
    pre_order += node.val
  pre_order_traversal(node.left)
  pre_order_traversal(node.right)


## 2. in-order
in_order = ''
def in_order_traversal(node):
  global in_order
  if not node:
    return 

  in_order_traversal(node.left)
  if node.val != '.':
    in_order += node.val
  in_order_traversal(node.right)


## 3. post-order
post_order = ''
def post_order_traversal(node):
  global post_order
  if not node:
    return 
  
  post_order_traversal(node.left)
  post_order_traversal(node.right)
  if node.val != '.':
    post_order += node.val


pre_order_traversal(root)
in_order_traversal(root)
post_order_traversal(root)
print(pre_order)
print(in_order)
print(post_order)