class Heap:
    def __init__(self, array):
        self.array = array
        self.size = len(array)

    def heapify(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.size and self.array[left] > self.array[largest]:
            largest = left

        if right < self.size and self.array[right] > self.array[largest]:
            largest = right

        if largest != index:
            self.array[index], self.array[largest] = self.array[largest], self.array[index]
            self.heapify(largest)

    def build_max_heap(self):
        for i in range(self.size // 2 - 1, -1, -1):
            self.heapify(i)

    def sort(self):
        self.build_max_heap()
        for i in range(self.size - 1, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.size -= 1
            self.heapify(0)
        return self.array


def heap_sort(array):
    heap = Heap(array)
    return heap.sort()