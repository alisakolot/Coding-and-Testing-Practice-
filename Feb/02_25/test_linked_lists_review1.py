import pytest
from linked_lists_review1 import * 

class TestLinkedList:

    def setup_method(self):
        self.prepared_linked_list = LinkedList()
        self.prepared_linked_list.insert(5)
        self.prepared_linked_list.insert(10)
        self.prepared_linked_list.insert(15)

        assert list(self.prepared_linked_list) == [5, 10, 15]

# trolling github because i like the bright green squares