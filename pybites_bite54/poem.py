INDENTS = 4


def print_hanging_indents(poem: str):
    paragraph, _, remainder = poem.partition("\n\n")

    for i, line in enumerate(paragraph.splitlines()):
        line = line.strip()
        print(" " * INDENTS + line) if i > 0 else print(line)

    if remainder:
        print_hanging_indents(remainder)
