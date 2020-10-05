import unittest


def is_binary_search_tree(root,lower_bound=-float('inf'),upper_bound=float('inf')):
    # Determine if the tree is a valid binary search tree

    # Binary trees have a few interesting properties when they're perfect:
    #
    # Property 1: the number of total nodes on each "level" doubles as we move down the tree.
    # Property 2: the number of nodes on the last level is equal to the sum of the number of nodes on all other levels
    # (plus 1). In other words, about half of our nodes are on the last level.

    # return condition
    if not root:
        return True
    # check if a node is bigger than a lower bound and smaller than a upper bound
    if root.value > lower_bound and root.value < upper_bound:
        return(is_binary_search_tree(root.right,root.value,upper_bound) and is_binary_search_tree(root.left,lower_bound, root.value))
    else:
        # binary search tree condition failure
        return False


# There is one more solution - iterative. Initialize a stack with a root. Then add right and left nodes values to it.















# Tests

class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_valid_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_both_subtrees_valid(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(60)
        right.insert_left(70)
        right.insert_right(90)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_out_of_order_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(70)
        right_right = right.insert_right(60)
        right_right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_one_node_tree(self):
        tree = Test.BinaryTreeNode(50)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)