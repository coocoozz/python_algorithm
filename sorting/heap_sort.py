import sys
sys.path.insert(0, "../data_structure")
import heap

class HeapSort:
    def __init__(self, list):
        self.list = list

    def ascending(self):
        ret = list()
        h = heap.Heap(False)
        for val in self.list:
            h.insert(val)

        for i in range(len(self.list)):
            ret.append(h.remove())

        return ret

    def descending(self):
        ret = list()
        h = heap.Heap(True)
        for val in self.list:
            h.insert(val)

        for i in range(len(self.list)):
            ret.append(h.remove())

        return ret
