STACK_REPR = '''
+-----+
| {i} |
+-----+
'''

class Stack:

    def __init__(self):
        self.stack = []


    def __len__(self):
        return len(self.stack)


    def __del__(self):
    """
    To delete an item at any position in a stack.
    """
        pass


    def __str__(self):
        pass


    def pretty_print(self):
        pass


    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        # TODO raise exceptions


    def push(self, item):
        self.stack.append(item)


    def create_stack(self, items):
        self.stack = items
