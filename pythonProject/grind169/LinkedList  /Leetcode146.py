# 146. LRU Cache
# double linkedlist/hashmap
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        # 加node後要重新定義前後箭頭關係
        previous_node = self.tail.prev
        previous_node.next = node
        node.prev = previous_node
        node.next = self.tail
        self.tail.prev = node

    def _remove_node(self, node):
        previous_node = node.prev
        previous_node.next = node.next
        node.next.prev = previous_node

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        node = self.lookup[key]
        self._remove_node(node)
        self._add_node(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self._remove_node(self.lookup[key])
        elif self.capacity == len(self.lookup):
            lru = self.head.next
            self._remove_node(lru)
            del self.lookup[lru.key]

        new_node = Node(key, value)
        self._add_node(new_node)
        self.lookup[new_node.key] = new_node
