import re
from collections import Counter


def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    counts = Counter(sequence.upper())
    gc_content = counts.get("G", 0) + counts.get("C", 0)
    at_content = counts.get("A", 0) + counts.get("T", 0)
    return round(gc_content * 100 / (gc_content + at_content), 2)