class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.nt = None  # Using 'nt' as you did for next

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        # DUMMY NODES: These stay forever and simplify everything
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.nt = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # Because of dummies, prev and nt are NEVER None
        prev_node = node.prev
        next_node = node.nt
        prev_node.nt = next_node
        next_node.prev = prev_node

    def _add_item(self, node):
        # Always insert right before the dummy tail (Most Recently Used)
        before_tail = self.tail.prev
        
        before_tail.nt = node
        node.prev = before_tail
        node.nt = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_item(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove the old node before adding the updated one
            self._remove(self.cache[key])
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_item(new_node)

        if len(self.cache) > self.cap:
            # The REAL oldest node is right after the dummy head
            lru = self.head.nt
            self._remove(lru)
            del self.cache[lru.key] # This is why we need node.key!