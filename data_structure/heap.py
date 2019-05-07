class Heap:
    def __init__(self, is_max_heap):
        self.list = list()
        self.is_max_heap = is_max_heap

    def swap(self, index1, index2):
        val = self.list[index1]
        self.list[index1] = self.list[index2]
        self.list[index2] = val

    def print(self):
        print(self.list)

    def insert_max_heap(self, value):
        self.list.append(value)
        cur_index = len(self.list) - 1
        while cur_index > 0:
            parent_index = int((cur_index - 1) / 2)
            if self.list[cur_index] > self.list[parent_index]:
                self.swap(cur_index, parent_index)
                cur_index = parent_index
            else:
                break

    def insert_min_heap(self, value):
        self.list.append(value)
        cur_index = len(self.list) - 1
        while cur_index > 0:
            parent_index = int((cur_index - 1) / 2)
            if self.list[cur_index] < self.list[parent_index]:
                self.swap(cur_index, parent_index)
                cur_index = parent_index
            else:
                break

    def remove_max_heap(self):
        ret = self.list[0]
        self.list[0] = self.list[len(self.list) - 1]
        del self.list[len(self.list) - 1]

        cur_index = 0
        while cur_index < len(self.list):
            next_index = cur_index
            for i in [1, 2]:
                child_index = cur_index * 2 + i
                if child_index < len(self.list) and self.list[next_index] < self.list[child_index]:
                    next_index = child_index
                else:
                    break

            if cur_index != next_index:
                self.swap(cur_index, next_index)
                cur_index = next_index
            else:
                break

        return ret

    def remove_max_heap(self):
        ret = self.list[0]
        self.list[0] = self.list[len(self.list) - 1]
        del self.list[len(self.list) - 1]

        cur_index = 0
        while cur_index < len(self.list):
            left_child_index = cur_index * 2 + 1
            if left_child_index >= len(self.list):
                break

            next_index = left_child_index

            right_child_index = cur_index * 2 + 2
            if right_child_index < len(self.list) and self.list[right_child_index] > self.list[left_child_index]:
                next_index = right_child_index

            if self.list[cur_index] < self.list[next_index]:
                self.swap(cur_index, next_index)
                cur_index = next_index
            else:
                break

        return ret

    def remove_min_heap(self):
        ret = self.list[0]
        self.list[0] = self.list[len(self.list) - 1]
        del self.list[len(self.list) - 1]

        cur_index = 0
        while cur_index < len(self.list):
            left_child_index = cur_index * 2 + 1
            if left_child_index >= len(self.list):
                break

            next_index = left_child_index

            right_child_index = cur_index * 2 + 2
            if right_child_index < len(self.list) and self.list[right_child_index] < self.list[left_child_index]:
                next_index = right_child_index

            if self.list[cur_index] > self.list[next_index]:
                self.swap(cur_index, next_index)
                cur_index = next_index
            else:
                break

        return ret

    def insert(self, value):
        if self.is_max_heap is True:
            return self.insert_max_heap(value)
        else:
            return self.insert_min_heap(value)

    def remove(self):
        if self.is_max_heap is True:
            return self.remove_max_heap()
        else:
            return self.remove_min_heap()
