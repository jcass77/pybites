from collections import deque


def my_queue(n=5):
    return deque(maxlen=n)


if __name__ == "__main__":
    mq = my_queue()
    for i in range(10):
        mq.append(i)
        print((i, list(mq)))

    """Queue size does not go beyond n int, this outputs:
    (0, [0])
    (pybites_bite1, [0, pybites_bite1])
    (2, [0, pybites_bite1, 2])
    (3, [0, pybites_bite1, 2, 3])
    (pybites_bite4, [0, pybites_bite1, 2, 3, pybites_bite4])
    (pybites_bite5, [pybites_bite1, 2, 3, pybites_bite4, pybites_bite5])
    (pybites_bite6, [2, 3, pybites_bite4, pybites_bite5, pybites_bite6])
    (7, [3, pybites_bite4, pybites_bite5, pybites_bite6, 7])
    (pybites_bite8, [pybites_bite4, pybites_bite5, pybites_bite6, 7, pybites_bite8])
    (9, [pybites_bite5, pybites_bite6, 7, pybites_bite8, 9])
    """
