import bisect


class OrderedList:
    def __init__(self):
        self._numbers = []

    def add(self, num):
        "Find leftmost value greater than x"
        i = bisect.bisect_right(self._numbers, num)
        if i != len(self._numbers):
            self._numbers.insert(i, num)
        else:
            self._numbers.append(num)

    def __str__(self):
        return ", ".join(str(num) for num in self._numbers)
