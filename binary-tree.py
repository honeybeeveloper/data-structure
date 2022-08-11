class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.__insert_data(self.root, data)

    def __insert_data(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self.__insert_data(node.left, data)
            else:
                node.right = self.__insert_data(node.right, data)
        return node

    def find(self, data):
        return self.__find_data(self.root, data)

    def __find_data(self, node, data):
        if node is None or node.data == data:
            return node is not None
        elif data <= node.data:
            return self.__find_data(node.left, data)
        else:
            return self.__find_data(node.right, data)

    def delete(self, data):
        self.root, deleted = self.__delete_data(self.root, data)
        return deleted

    def __delete_data(self, node, data):
        if node is None:
            return node, False

        if data == node.data:
            deleted = True
            # 왼쪽, 오른쪽 모두 있을 때 이동
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.right
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            # 왼쪽 이나 오른쪽 한 곳만 있을 때
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif data < node.data:
            node.left, deleted = self.__delete_data(node.left, data)
        else:
            node.right, deleted = self.__delete_data(node.right, data)
        return node, deleted

    def preorder_traverse(self):
        """
        전위 순회 : 루트를 먼저 방문 (루트->왼쪽트리->오른쪽트리)
        """
        def __preorder_traverse(root):
            if root is None:
                pass
            else:
                print(root.data, end=' ')
                __preorder_traverse(root.left)
                __preorder_traverse(root.right)
        __preorder_traverse(self.root)

    def inorder_traverse(self):
        """
        중위 순회 : 왼쪽 하위 트리를 방문 후 루트를 방문 (왼쪽트리->루트->오른쪽트리)
        """
        def __inorder_traverse(root):
            if root is None:
                pass
            else:
                __inorder_traverse(root.left)
                print(root.data, end=' ')
                __inorder_traverse(root.right)
        __inorder_traverse(self.root)

    def postorder_traverse(self):
        """
        후위 순회 : 하위 트리를 모두 방문 후 루트를 방문 (왼쪽트리->오른쪽트리->루트)
        """
        def __postorder_traverse(root):
            if root is None:
                pass
            else:
                __postorder_traverse(root.left)
                __postorder_traverse(root.right)
                print(root.data, end=' ')
        __postorder_traverse(self.root)

    def level_order_traverse(self):
        """
        층별 순회(너비우선탐색) : 위 노드들부터 아래 방향으로 차례로 방문 (뿌리노드부터 깊이 순으로 방문)
        """
        def __level_order_traverse(root):
            queue = [root]
            while queue:
                root = queue.pop(0)
                if root is not None:
                    print(root.data, end=' ')
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
        __level_order_traverse(self.root)


if __name__ == '__main__':
    data = [20, 6, 8, 12, 78, 32, 65, 32, 7, 9]
    tree = BinaryTree()

    for d in data:
        tree.insert(d)
    print('find!')
    print(tree.find(9))
    print(tree.find(12))
    print(tree.find(11))
    print(tree.find(65))
    print('delete!')
    print(tree.delete(78))
    print(tree.delete(6))
    print(tree.delete(11))
    print(tree.delete(18))

    print('preorder_traverse')
    tree.preorder_traverse()
    print('\ninorder_traverse')
    tree.inorder_traverse()
    print('\npostorder_traverse')
    tree.postorder_traverse()
    print('\nlevel_order_traverse')
    tree.level_order_traverse()

