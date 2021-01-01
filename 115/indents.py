def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    count = 0
    for char in text:
        if char != " ":
            return count

        count += 1
