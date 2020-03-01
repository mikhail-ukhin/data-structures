
class Stack:

    def __init__(self):
        self._count = 0
        self._head = None

    def push(self, value):
        if not value:
            raise ValueError('value should not be none')

        if not self._head:
            self._head = value
        else:
            value.parent = self._head
            self._head = value

        self._count = self._count + 1

    def pop(self):
        if not self._head:
            raise ReferenceError('stack is empty')
        else:
            previous_head = self._head
            self._head = self._head.parent
            self._count = self._count - 1

            return previous_head

    def top(self):
        return self._head;

    def empty(self):
        return self._count == 0

    def count(self):
        return self._count
