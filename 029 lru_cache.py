class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity

        # Dictionary: key -> Node
        self.cache = {}

        # Dummy nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove a node from the linked list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # Add a node just before tail
    # This means the node becomes Most Recently Used
    def add_to_mru(self, node):
        last_node = self.tail.prev

        last_node.next = node
        node.prev = last_node

        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        # Key doesn't exist
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move node to MRU position
        self.remove(node)
        self.add_to_mru(node)

        return node.value

    def put(self, key, value):
        # Key already exists
        if key in self.cache:
            node = self.cache[key]

            # Update value
            node.value = value

            # Move to MRU
            self.remove(node)
            self.add_to_mru(node)

            return

        # Create new node
        node = Node(key, value)

        # Store in dictionary
        self.cache[key] = node

        # Add as MRU
        self.add_to_mru(node)

        # If capacity exceeded
        if len(self.cache) > self.capacity:
            # Least Recently Used node
            lru_node = self.head.next

            self.remove(lru_node)

            # Remove from dictionary
            del self.cache[lru_node.key]


# -------------------------
# Test
# -------------------------

cache = LRUCache(3)

cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")

print(cache.get(1))   # A

cache.put(4, "D")

print(cache.get(2))   # -1
print(cache.get(3))   # C
print(cache.get(4))   # D