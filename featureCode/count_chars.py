def count_chars_with_whitespace(input: str):
    "just returns the number of chars"
    return len(input)

def count_chars_ignore_whitespace(input: str):
    "ignores unnecessary whitespace for counting chars"
    input=" ".join(input.split())
    return count_chars_with_whitespace(input)


def count_chars_with_whitespace(input: str):
    return len(input)