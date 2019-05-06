class BubbleSort:
    def __init__(self, list):
        self.list = list

    def swap(self, index1, index2):
        val = self.list[index1]
        self.list[index1] = self.list[index2]
        self.list[index2] = val

    def ascending(self):
        changed = False
        for last_index in range(len(self.list)-1, 0, -1):
            cur_index = 1
            while cur_index <= last_index:
                if self.list[cur_index] < self.list[cur_index-1]:
                    self.swap(cur_index, cur_index-1)
                    changed = True
                cur_index += 1

            if changed is False:
                break

        return self.list

    def descending(self):
        changed = False
        for last_index in range(len(self.list)-1, 0, -1):
            cur_index = 1
            while cur_index <= last_index:
                if self.list[cur_index] > self.list[cur_index-1]:
                    self.swap(cur_index, cur_index-1)
                    changed = True
                cur_index += 1

            if changed is False:
                break

        return self.list
