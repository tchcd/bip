# * 1.8. Напишите функцию, которая получает на вход два связанных списка,
# состоящие из целых значений, и если их длины равны, возвращает список,
# каждый элемент которого равен сумме соответствующих элементов входных списков.

from typing import Union, List


class Node:
    def __init__(self, value: Union[str, int, float]):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, item: Node) -> None:
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self) -> None:
        node = self.head
        while node:
            print(node)
            node = node.next

    def len(self) -> int:
        node = self.head
        cnt = 0
        while node:
            cnt += 1
            node = node.next
        return cnt

    def get_all_items(self) -> list:
        node = self.head
        elements = []
        while node:
            elements.append(node.value)
            node = node.next
        return elements


def sum_linked_lists_elements(first: LinkedList, second: LinkedList) -> List[float]:
    """
    Compares the length of two linked lists and,
    if they are the same length, returns the sum of their elements
    """
    if not isinstance(first, LinkedList) or not isinstance(first, LinkedList):
        raise ValueError('Arguments must be a LinkedList class!')

    if first.len() != second.len() and first.len() <= 0:
        raise ValueError('LinkedLists must be a same length and contain at least one element!')

    try:
        first_elements = map(float, first.get_all_items())
        second_elements = map(float, second.get_all_items())
        sum_of_elements = [sum(i) for i in zip(first_elements, second_elements)]
    except ValueError:
        print('LinkedLists must contain numeric elements')
        raise

    return sum_of_elements


if __name__ == "__main__":
    n1 = Node(-1)
    n2 = Node(-2)
    n3 = Node(-3)
    n4 = Node(1)
    n5 = Node(2)
    n6 = Node(3)

    negative_linked_list = LinkedList()
    negative_linked_list.add_to_tail(n1)
    negative_linked_list.add_to_tail(n2)
    negative_linked_list.add_to_tail(n3)

    positive_linked_list = LinkedList()
    positive_linked_list.add_to_tail(n4)
    positive_linked_list.add_to_tail(n5)
    positive_linked_list.add_to_tail(n6)

    print(sum_linked_lists_elements(negative_linked_list, positive_linked_list))

