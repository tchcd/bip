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
        self.assertEqual(node2.prev, None)
        self.assertEqual(node3.prev, node2)
        self.assertEqual(node4.prev, node3)

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
        self.assertEqual(node1.prev, None)
        self.assertEqual(node3.prev, node1)

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
        self.assertEqual(node1.prev, None)

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
        self.assertEqual(node1.prev, None)
        self.assertEqual(node2.prev, node1)
        self.assertEqual(node3.prev, node2)

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
        self.assertEqual(node1.prev, None)

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
        self.assertEqual(node3.prev, None)
        self.assertEqual(node4.prev, node3)

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
        self.assertEqual(node2.prev, None)
        self.assertEqual(node4.prev, node2)
        self.assertEqual(node6.prev, node4)

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
        self.assertEqual(node1.prev, None)
        self.assertEqual(node2.prev, node1)
        self.assertEqual(node3.prev, node2)

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
        self.assertEqual(node2.prev, None)


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
        self.assertEqual(node1.prev, None)


    ###############################################
    #Если afterNode = None и список пустой, добавьте новый элемент первым в списке
    #Если afterNode = None и список непустой, добавьте новый элемент последним в списке.
    #Добавьте в класс LinkedList2 метод вставки узла после заданного узла.

    ## Тесты для insert
    # пустой список (+afterNode = None)
    # один элемент в начало, в конец, (+afterNode = None)
    # перед последним
    # после последнего
    # в середину

    # Если afterNode = None и список пустой, добавьте новый элемент первым в списке
    def test_insert_empty_list_after_node_none(self):
        empty_ll = LinkedList2()
        n1 = Node(1)

        empty_ll.insert(afterNode=None, newNode=n1)
        self.assertEqual(self._get_values(empty_ll), [1])
        self.assertEqual(empty_ll.head, n1)
        self.assertEqual(empty_ll.tail, n1)
        self.assertEqual(n1.prev, None)

    def test_insert_to_start(self):
        ll = LinkedList2()
        n1 = Node(1)
        n0 = Node(0)
        ll.add_in_tail(n1)

        ll.insert(afterNode=n1, newNode=n0)
        self.assertEqual(self._get_values(ll), [1, 0])
        self.assertEqual(ll.head, n1)
        self.assertEqual(ll.tail, n0)
        self.assertEqual(n1.prev, None)
        self.assertEqual(n0.prev, n1)


    def test_insert_to_start_after_none(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n0 = Node(0)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)

        ll.insert(afterNode=None, newNode=n0)
        self.assertEqual(self._get_values(ll), [1, 2, 0])
        self.assertEqual(ll.head, n1)
        self.assertEqual(ll.tail, n0)
        self.assertEqual(n1.prev, None)
        self.assertEqual(n2.prev, n1)
        self.assertEqual(n0.prev, n2)

#Если afterNode = None и список непустой, добавьте новый элемент последним в списке.
    def test_insert_to_mid_with_none(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)

        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.add_in_tail(n3)

        ll.insert(afterNode=None, newNode=n4)
        self.assertEqual(self._get_values(ll), [1, 2, 3, 4])
        self.assertEqual(ll.head, n1)
        self.assertEqual(ll.tail, n4)
        self.assertEqual(n1.prev, None)
        self.assertEqual(n2.prev, n1)
        self.assertEqual(n3.prev, n2)
        self.assertEqual(n4.prev, n3)

    def test_insert_to_mid(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n0 = Node(0)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.add_in_tail(n3)
        ll.add_in_tail(n4)

        ll.insert(afterNode=n3, newNode=n0)
        self.assertEqual(self._get_values(ll), [1, 2, 3, 0, 4])
        self.assertEqual(ll.head, n1)
        self.assertEqual(ll.tail, n4)

        self.assertEqual(n1.prev, None)
        self.assertEqual(n2.prev, n1)
        self.assertEqual(n3.prev, n2)
        self.assertEqual(n0.prev, n3)
        self.assertEqual(n4.prev, n0)

    def test_insert_to_end(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n0 = Node(0)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.add_in_tail(n3)

        ll.insert(afterNode=n3, newNode=n0)
        self.assertEqual(self._get_values(ll), [1, 2, 3, 0])
        self.assertEqual(ll.head, n1)
        self.assertEqual(ll.tail, n0)
        self.assertEqual(n1.prev, None)
        self.assertEqual(n2.prev, n1)
        self.assertEqual(n3.prev, n2)
        self.assertEqual(n0.prev, n3)

    def test_add_in_head_empty(self):
        ll = LinkedList2()
        n0 = Node(0)

        ll.add_in_head(newNode=n0)
        self.assertEqual(self._get_values(ll), [0])
        self.assertEqual(ll.head, n0)
        self.assertEqual(ll.tail, n0)
        self.assertEqual(n0.prev, None)

    def test_add_in_head_one(self):
        ll = LinkedList2()
        n1 = Node(1)
        n0 = Node(0)
        ll.add_in_tail(n1)

        ll.add_in_head(newNode=n0)
        self.assertEqual(self._get_values(ll), [0, 1])
        self.assertEqual(ll.head, n0)
        self.assertEqual(ll.tail, n1)
        self.assertEqual(n0.prev, None)
        self.assertEqual(n1.prev, n0)

    def test_add_in_head_seq_same(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(1)
        n0 = Node(0)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)

        ll.add_in_head(newNode=n0)
        self.assertEqual(self._get_values(ll), [0, 1, 1])
        self.assertEqual(ll.head, n0)
        self.assertEqual(ll.tail, n2)
        self.assertEqual(n0.prev, None)
        self.assertEqual(n1.prev, n0)
        self.assertEqual(n2.prev, n1)

    def test_add_in_head_seq_diff(self):
        ll = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n0 = Node(0)
        ll.add_in_tail(n1)
        ll.add_in_tail(n2)

        ll.add_in_head(newNode=n0)
        self.assertEqual(self._get_values(ll), [0, 1, 2])
        self.assertEqual(ll.head, n0)
        self.assertEqual(ll.tail, n2)
        self.assertEqual(n0.prev, None)
        self.assertEqual(n1.prev, n0)
        self.assertEqual(n2.prev, n1)

    def test_len_empty_list(self):
        empty_ll = LinkedList2()
        self.assertEqual(empty_ll.len(), 0)
        self.assertEqual(empty_ll.head, None)
        self.assertEqual(empty_ll.tail, None)

    def test_len_one_el_list(self):
        n0 = Node(0)
        one_el_ll = LinkedList2()
        one_el_ll.add_in_tail(n0)
        self.assertEqual(one_el_ll.len(), 1)
        self.assertEqual(one_el_ll.head, n0)
        self.assertEqual(one_el_ll.tail, n0)

    def test_len_several_el_list(self):
        n0 = Node(0)
        n1 = Node(2)
        n2 = Node(4)
        n3 = Node(4)
        one_el_ll = LinkedList2()
        one_el_ll.add_in_tail(n0)
        one_el_ll.add_in_tail(n1)
        one_el_ll.add_in_tail(n2)
        one_el_ll.add_in_tail(n3)
        self.assertEqual(one_el_ll.len(), 4)
        self.assertEqual(one_el_ll.head, n0)
        self.assertEqual(one_el_ll.tail, n3)

    def test_clean_empty_list(self):
        empty_ll = LinkedList2()
        empty_ll.clean()

        self.assertEqual(self._get_values(empty_ll), [])
        self.assertEqual(empty_ll, empty_ll)
        self.assertEqual(empty_ll.tail, None)
        self.assertEqual(empty_ll.head, None)

    def test_clean_one_element_list(self):
        one_el_ll = LinkedList2()
        n0 = Node(0)
        one_el_ll.add_in_tail(n0)

        one_el_ll.clean()

        self.assertEqual(self._get_values(one_el_ll), [])
        self.assertEqual(one_el_ll, one_el_ll)
        self.assertEqual(one_el_ll.tail, None)
        self.assertEqual(one_el_ll.head, None)

    def test_clean_several_elements(self):
        ll = LinkedList2()
        n1 = Node(3)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(3)

        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.add_in_tail(n3)
        ll.add_in_tail(n4)
        ll.add_in_tail(n5)

        ll.clean()

        self.assertEqual(self._get_values(ll), [])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.tail, None)
        self.assertEqual(ll.head, None)


    def test_find_all_first_middle_last(self):
        ll = LinkedList2()
        n1 = Node(3)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(3)

        ll.add_in_tail(n1)
        ll.add_in_tail(n2)
        ll.add_in_tail(n3)
        ll.add_in_tail(n4)
        ll.add_in_tail(n5)

        self.assertEqual(ll.find_all(3), [n1, n3, n5])
        self.assertEqual(ll.head, n1)
        self.assertEqual(ll.tail, n5)

    def test_find_all_empty_list(self):
        empty_ll = LinkedList2()
        self.assertEqual(empty_ll.find_all(3), [])
        self.assertEqual(empty_ll.head, None)
        self.assertEqual(empty_ll.tail, None)

    def test_find_all_one_el(self):
        one_el_ll = LinkedList2()
        n0 = Node(0)
        one_el_ll.add_in_tail(n0)
        self.assertEqual(one_el_ll.find_all(0), [n0])
        self.assertEqual(one_el_ll.head, n0)
        self.assertEqual(one_el_ll.tail, n0)


if __name__ == "__main__":
    unittest.main()
