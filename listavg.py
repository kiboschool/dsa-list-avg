class ListAverage:
    def __init__(self, lst):
        self.lst = lst.copy()
        self.total = 0

    def add(self, num):
        self.lst.append(num)
        self.total += num

    def compute_avg(self):
        total = 0
        for num in self.lst:
            total += num
        return total / len(self.lst)

    def compute_avg_faster(self):
        return total / len(self.lst)
