def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
    returns a sequence of same length with the averages.
    You can assume all items in sequence are numeric."""

    return (round(sum(sequence[0:i]) / i, 2) for i in range(1, len(sequence) + 1))
