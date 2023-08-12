import unittest
from linked_list_main import LinkedList, Node
import linked_list_additional as lla


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @staticmethod
    def _get_values(ll: LinkedList):
        result = []
        node = ll.head
        while node is not None:
            result.append(node.value)
            node = node.next
        return result

    @staticmethod
    def _create_empty_ll():
        return LinkedList()

    def test_find_all_first_middle_last(self):
        ll = LinkedList()
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
        empty_ll = LinkedList()
        self.assertEqual(empty_ll.find_all(3), [])
        self.assertEqual(empty_ll.head, None)
        self.assertEqual(empty_ll.tail, None)

    def test_find_all_one_el(self):
        one_el_ll = LinkedList()
        n0 = Node(0)
        one_el_ll.add_in_tail(n0)
        self.assertEqual(one_el_ll.find_all(0), [n0])
        self.assertEqual(one_el_ll.head, n0)
        self.assertEqual(one_el_ll.tail, n0)

    ## Тесты для delete()
    # + первая
    # + последняя
    # + пустой и один элемент
    ## all = True.
    # + две одинаковые подряд
    # + две одинаковые через одну
    # + одинаковые в начале и в конце
    # + все одинаковые
    # + не существующий

    def test_delete_remove_first(self):
        ll = LinkedList()
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

    def test_delete_remove_last(self):
        ll = LinkedList()
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
        ll = LinkedList()

        ll.delete(3)

        self.assertEqual(self._get_values(ll), [])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

    def test_delete_remove_from_one_el_list(self):
        ll = LinkedList()
        node1 = Node(0)
        ll.add_in_tail(node1)

        ll.delete(1)

        self.assertEqual(self._get_values(ll), [0])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.head, node1)
        self.assertEqual(ll.tail, node1)

    def test_delete_remove_being_from_one_el_list(self):
        ll = LinkedList()
        node1 = Node(0)
        ll.add_in_tail(node1)

        ll.delete(0)

        self.assertEqual(self._get_values(ll), [])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

    def test_delete_remove_two_same_sequential(self):
        ll = LinkedList()
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
        ll = LinkedList()
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
        ll = LinkedList()
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
        ll = LinkedList()
        node1 = Node(1)
        node2 = Node(1)
        node3 = Node(1)
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        ll.add_in_tail(node3)

        ll.delete(2, all=True)

        self.assertEqual(self._get_values(ll), [1,1, 1])
        self.assertEqual(ll, ll)
        self.assertEqual(ll.head, node1)
        self.assertEqual(ll.tail, node3)

    def test_delete_remove_first_and_last(self):
        ll = LinkedList()
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

    ## Тесты для clean()
    # + пустой
    # + один элемент
    # + много одинаковых элементов

    def test_clean_empty_list(self):
        empty_ll = LinkedList()
        empty_ll.clean()

        self.assertEqual(self._get_values(empty_ll), [])
        self.assertEqual(empty_ll, empty_ll)
        self.assertEqual(empty_ll.tail, None)
        self.assertEqual(empty_ll.head, None)

    def test_clean_one_element_list(self):
        one_el_ll = LinkedList()
        n0 = Node(0)
        one_el_ll.add_in_tail(n0)

        one_el_ll.clean()

        self.assertEqual(self._get_values(one_el_ll), [])
        self.assertEqual(one_el_ll, one_el_ll)
        self.assertEqual(one_el_ll.tail, None)
        self.assertEqual(one_el_ll.head, None)

    def test_clean_several_elements(self):
        ll = LinkedList()
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

    ## Тесты для len()
    # + пустой и один элемент
    # + Передать много одинаковых элементов

    def test_len_empty_list(self):
        empty_ll = LinkedList()
        self.assertEqual(empty_ll.len(), 0)
        self.assertEqual(empty_ll.head, None)
        self.assertEqual(empty_ll.tail, None)

    def test_len_one_el_list(self):
        n0 = Node(0)
        one_el_ll = LinkedList()
        one_el_ll.add_in_tail(n0)
        self.assertEqual(one_el_ll.len(), 1)
        self.assertEqual(one_el_ll.head, n0)
        self.assertEqual(one_el_ll.tail, n0)

    def test_len_several_el_list(self):
        n0 = Node(0)
        n1 = Node(2)
        n2 = Node(4)
        n3 = Node(4)
        one_el_ll = LinkedList()
        one_el_ll.add_in_tail(n0)
        one_el_ll.add_in_tail(n1)
        one_el_ll.add_in_tail(n2)
        one_el_ll.add_in_tail(n3)
        self.assertEqual(one_el_ll.len(), 4)
        self.assertEqual(one_el_ll.head, n0)
        self.assertEqual(one_el_ll.tail, n3)

    ## Тесты для insert
    # + пустой список (+afterNode = None)
    # + один элемент в начало, в конец, (+afterNode = None)
    # + перед последним
    # + после последнего
    # + в середину

    def test_insert_empty_list_after_node_none(self):
        empty_ll = LinkedList()
        n1 = Node(1)

        empty_ll.insert(afterNode=None, newNode=n1)
        self.assertEqual(self._get_values(empty_ll), [1])
        self.assertEqual(empty_ll.head, n1)
        self.assertEqual(empty_ll.tail, n1)

    def test_insert_to_start(self):
        ll = LinkedList()
        n1 = Node(1)
        n0 = Node(0)
        ll.add_in_tail(n1)

        ll.insert(afterNode=n1, newNode=n0)
        self.assertEqual(self._get_values(ll), [1, 0])
        self.assertEqual(ll.head, n1)
        self.assertEqual(ll.tail, n0)

    def test_insert_to_start_after_none(self):
        ll = LinkedList()
        n1 = Node(1)
        n0 = Node(0)
        ll.add_in_tail(n1)

        ll.insert(afterNode=None, newNode=n0)
        self.assertEqual(self._get_values(ll), [0, 1])
        self.assertEqual(ll.head, n0)
        self.assertEqual(ll.tail, n1)

    def test_insert_to_mid(self):
        ll = LinkedList()
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

    def test_insert_to_end(self):
        ll = LinkedList()
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


class TestLinkedListAdditonal(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_correct_head_and_tail_in_linked_list(self):
        llaa = lla.LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        llaa.add_to_tail(n1)
        llaa.add_to_tail(n2)
        llaa.add_to_tail(n3)
        self.assertEqual(llaa.head, n1)
        self.assertEqual(llaa.tail, n3)

    def test_sum_linked_lists_elements_with_not_correct_element(self):
        llpos = lla.LinkedList()
        llneg = lla.LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node('a')
        n5 = Node(-2)
        n6 = Node(-3)

        llpos.add_to_tail(n1)
        llpos.add_to_tail(n2)
        llpos.add_to_tail(n3)
        llneg.add_to_tail(n4)
        llneg.add_to_tail(n5)
        llneg.add_to_tail(n6)

        self.assertRaises(ValueError, lla.sum_linked_lists_elements, llpos, llneg)

    def test_sum_linked_lists_elements_with_correct_element(self):
        llpos = lla.LinkedList()
        llneg = lla.LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node('-1')
        n5 = Node(-2)
        n6 = Node(-3)

        llpos.add_to_tail(n1)
        llpos.add_to_tail(n2)
        llpos.add_to_tail(n3)
        llneg.add_to_tail(n4)
        llneg.add_to_tail(n5)
        llneg.add_to_tail(n6)

        self.assertEqual(lla.sum_linked_lists_elements(llpos, llneg), [0.0, 0.0, 0.0])



if __name__ == "__main__":
    unittest.main()
