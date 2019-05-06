class InsertSort:
    def __init__(self, list):
        self.list = list

    def swap(self, index1, index2):
        val = self.list[index1]
        self.list[index1] = self.list[index2]
        self.list[index2] = val

    def ascending(self):
        for index in range(1, len(self.list)):
            cur_index = index
            while cur_index > 0:
                if self.list[cur_index] > self.list[cur_index-1]:
                    break
                else:
                    self.swap(cur_index, cur_index-1)
                    cur_index -= 1
        return self.list

    def descending(self):
        for index in range(1, len(self.list)):
            cur_index = index
            while cur_index > 0:
                if self.list[cur_index] < self.list[cur_index-1]:
                    break
                else:
                    self.swap(cur_index, cur_index-1)
                    cur_index -= 1
        return self.list