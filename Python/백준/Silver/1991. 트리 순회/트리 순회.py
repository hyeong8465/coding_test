"""
16:01
전위: bfs
중위: 왼 - 루 - 오
후위: 왼 - 오 - 루

직접 구현하기


"""
n = int(input())
tree = {}
idx = 0
for _ in range(n):
    x, y, z = input().split()
    tree[x] = (y,z)

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')

        