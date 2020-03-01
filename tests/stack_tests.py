import unittest
from structures import stack, node


class TestStack(unittest.TestCase):

    def test__count__empty_stack__return_zero(self):
        s = stack.Stack()

        self.assertEqual(s.count(), 0)

    def test__count__pop_from_stack_return_one(self):
        s = stack.Stack()
        n1 = node.Node(1)
        n2 = node.Node(2)

        s.push(n1)
        s.push(n2)

        s.pop()

        self.assertEqual(s.count(), 1)

    def test__push__add_element__count_should_be_one(self):
        s = stack.Stack()
        n = node.Node(1)

        s.push(n)

        self.assertEqual(s.count(), 1)

    def test__push__add_some_elements__count_should_be_two(self):
        s = stack.Stack()
        n1 = node.Node(1)
        n2 = node.Node(2)

        s.push(n1)
        s.push(n2)

        self.assertEqual(s.count(), 2)

    def test__push__add_empty_element__raise_exception(self):
        s = stack.Stack()
        n = None

        self.assertRaises(ValueError, lambda: s.push(n))

    def test__empty__empty_stack__return_true(self):
        s = stack.Stack()

        self.assertTrue(s.empty())

    def test__empty__empty_stack__return_false(self):
        s = stack.Stack()
        n = node.Node(1)

        s.push(n)

        self.assertFalse(s.empty())

    def test__top__empty_stack__return_none(self):
        s = stack.Stack()

        self.assertEqual(s.top(), None)

    def test__top__not_empty_stack__return_last_element(self):
        s = stack.Stack()
        n = node.Node(1)

        s.push(n)
        top = s.top()

        self.assertEqual(top.value, 1)

    def test__pop__empty_stack__raise_reference_exception(self):
        s = stack.Stack()

        self.assertRaises(ReferenceError, lambda: s.pop())

    def test__pop__not_empty_stack__return_node_two(self):
        s = stack.Stack()
        n1 = node.Node(1)
        n2 = node.Node(2)

        s.push(n1)
        s.push(n2)

        top = s.pop()

        self.assertEqual(top.value, 2)


if __name__ == '__main__':
    unittest.main()
