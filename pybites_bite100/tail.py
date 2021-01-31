def tail(filepath, n):
    """Simulate Unix' tail -n, read in filepath, parse it into a list,
    strip newlines and return a list of the last n lines"""
    with open(filepath) as f:
        content = f.read()
        return content.splitlines()[-n:]
