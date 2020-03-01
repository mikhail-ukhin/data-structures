class Node:
    def __init__(self, value):
        if not value:
            raise ValueError('value should not be none')

        self.parent = None
        self.value = value
