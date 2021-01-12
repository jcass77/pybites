INDENTS = 4


def print_hanging_indents(poem: str):
    para, _, remainder = poem.strip().partition("\n\n")

    for i, line in enumerate(para.splitlines()):
        line = line.strip()
        # Don't print indents for first iteration
        print(line.rjust(len(line) + min(i, 1) * INDENTS))

    if remainder:
        print_hanging_indents(remainder)
