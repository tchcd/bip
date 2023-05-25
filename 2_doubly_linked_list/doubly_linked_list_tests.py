import unittest
from doubly_linked_list_main import LinkedList2, Node



class TestLinkedList2(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @staticmethod
    def _get_values(ll: LinkedList2):
        result = []
        node = ll.head
        while node is not None:
            result.append(node.value)
            node = node.next
        return result

    def test_delete_remove_first(self):
        ll = LinkedList2()
        node1 = Node(1)
        node2 = Node(1)
        node3 = Node(2)
        node4 = Node(3)
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        ll.add_in_tail(node3)
        ll.add_in_tail(node4)

        ll.delete(1)

        self.assertEqual(self._get_values(ll), [1, 2, 3])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.head, node2)
        self.assertEqual(ll.tail, node4)

    def test_delete_remove_first_middle(self):
        ll = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(2)
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        ll.add_in_tail(node3)

        ll.delete(2)

        self.assertEqual(self._get_values(ll), [1, 2])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.head, node1)
        self.assertEqual(ll.tail, node3)

    def test_delete_remove_second(self):
        ll = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)

        ll.delete(2)

        self.assertEqual(self._get_values(ll), [1])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.head, node1)
        self.assertEqual(ll.tail, node1)

    def test_delete_remove_last(self):
        ll = LinkedList2()
        node1 = Node(1)
        node2 = Node(1)
        node3 = Node(2)
        node4 = Node(3)
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        ll.add_in_tail(node3)
        ll.add_in_tail(node4)

        ll.delete(3)

        self.assertEqual(self._get_values(ll), [1, 1, 2])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.head, node1)
        self.assertEqual(ll.tail, node3)

    def test_delete_remove_from_empty_list(self):
        ll = LinkedList2()

        ll.delete(3)

        self.assertEqual(self._get_values(ll), [])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

    def test_delete_remove_from_one_el_list(self):
        ll = LinkedList2()
        node1 = Node(0)
        ll.add_in_tail(node1)

        ll.delete(1)

        self.assertEqual(self._get_values(ll), [0])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.head, node1)
        self.assertEqual(ll.tail, node1)

    def test_delete_remove_being_from_one_el_list(self):
        ll = LinkedList2()
        node1 = Node(0)
        ll.add_in_tail(node1)

        ll.delete(0)

        self.assertEqual(self._get_values(ll), [])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

    def test_delete_remove_two_same_sequential(self):
        ll = LinkedList2()
        node1 = Node(1)
        node2 = Node(1)
        node3 = Node(2)
        node4 = Node(3)
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        ll.add_in_tail(node3)
        ll.add_in_tail(node4)

        ll.delete(1, all=True)

        self.assertEqual(self._get_values(ll), [2, 3])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.head, node3)
        self.assertEqual(ll.tail, node4)

    def test_delete_remove_same_through_one(self):
        ll = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(1)
        node4 = Node(3)
        node5 = Node(1)
        node6 = Node(4)
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        ll.add_in_tail(node3)
        ll.add_in_tail(node4)
        ll.add_in_tail(node5)
        ll.add_in_tail(node6)

        ll.delete(1, all=True)

        self.assertEqual(self._get_values(ll), [2, 3, 4])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.head, node2)
        self.assertEqual(ll.tail, node6)

    def test_delete_remove_same_seq_el(self):
        ll = LinkedList2()
        node1 = Node(1)
        node2 = Node(1)
        node3 = Node(1)
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        ll.add_in_tail(node3)

        ll.delete(1, all=True)

        self.assertEqual(self._get_values(ll), [])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

    def test_delete_remove_not_being_el(self):
        ll = LinkedList2()
        node1 = Node(1)
        node2 = Node(1)
        node3 = Node(1)
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        ll.add_in_tail(node3)

        ll.delete(2, all=True)

        self.assertEqual(self._get_values(ll), [1, 1, 1])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.head, node1)
        self.assertEqual(ll.tail, node3)

    def test_delete_remove_first_and_last(self):
        ll = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(1)
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        ll.add_in_tail(node3)

        ll.delete(1, all=True)

        self.assertEqual(self._get_values(ll), [2])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.head, node2)
        self.assertEqual(ll.tail, node2)

    def test_delete_remove_seq_last(self):
        ll = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(2)
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        ll.add_in_tail(node3)

        ll.delete(2, all=True)

        self.assertEqual(self._get_values(ll), [1])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.head, node1)
        self.assertEqual(ll.tail, node1)


if __name__ == "__main__":
    unittest.main()