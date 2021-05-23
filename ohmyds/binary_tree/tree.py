class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def __str__(self):
        tree_str_list =  self.pretty_print()
        tree_str = '\n'.join(tree_str_list)
        return tree_str


    def level_order(self):
        root = self
        queue = []
        queue.append(root)
        bfs = []

        while queue:
            level_queue = []
            count = len(queue)

            while count: 
                s = queue.pop(0)
                level_queue.append(s.val)

                if s.left:
                    queue.append(s.left)
                if s.right:
                    queue.append(s.right)

                count -= 1

            bfs.append(level_queue)

        return bfs


    def inorder(self):
        pass


    def postorder(self):
        pass


    def preorder(self):
        pass


    def pretty_print(self):
        lines, *_ = self.pretty_print_util()
        tree_str = []
        
        for line in lines:
            tree_str.append(line)


        return tree_str


    def pretty_print_util(self):
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left.pretty_print_util()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right.pretty_print_util()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.pretty_print_util()
        right, m, q, y = self.right.pretty_print_util()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def create_tree(vals):
    nodes = [Node(i) if i else None for i in vals]

    for i in range(1, len(nodes)):
        node = nodes[i]

        if node:
            parent_index = (i - 1) // 2
            parent = nodes[parent_index]
            
            if parent:
                if i % 2 == 0:
                    parent.left = node
                else:
                    parent.right = node

    return nodes[0]
