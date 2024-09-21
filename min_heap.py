class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) >> 1 if i > 0 else None

    def left(self, i):
        return (i << 1) + 1

    def right(self, i):
        return (i << 1) + 2

    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        smallest = i

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)

    def build_min_heap(self, arr):
        self.heap = arr

        for i in range((len(arr) >> 1) - 1, -1, -1):
            self.heapify(i)

    def get_root(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]

        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return root

    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1

        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    # Print the heap (optional helper for visualization)
    def print_heap(self):
        print(self.heap)


heap = MinHeap()

elements = [5, 13, 2, 25, 7, 17, 20, 8, 4, 5, 3, 17, 10, 84, 19, 6, 22, 9]
print(elements)
heap.build_min_heap(elements)
heap.print_heap()

print(f"Root: {heap.get_root()}")

heap.pop()
print(f"Heap after root pop:")
heap.print_heap()

print(f"Insert 0.5 into heap")
heap.insert(0.5)
heap.print_heap()

print(f"Root: {heap.get_root()}")

print(f"Insert 23 into heap")
heap.insert(23)
heap.print_heap()
