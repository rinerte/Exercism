import operator

def answer(question):
    known_operations = {
        "plus": operator.add,
        "minus": operator.sub,
        "multiplied": operator.mul,
        "divided": operator.floordiv,
    }

    if not question.startswith("What is") or not question.endswith("?"):
        raise ValueError("unknown operation")

    words = (
        question[7:-1]
        .replace("multiplied by", "multiplied")
        .replace("divided by", "divided")
        .split()
    )

    if not words:
        raise ValueError("syntax error")

    for i in range(0, len(words), 2):
        try:
            words[i] = int(words[i])
        except ValueError:
            raise ValueError("syntax error")

    for i in range(1, len(words), 2):
        if words[i] not in known_operations:
            try:
                int(words[i])
                raise ValueError("syntax error")
            except ValueError as e:
                if str(e) == "syntax error":
                    raise
                raise ValueError("unknown operation")

    if len(words) % 2 == 0:
        raise ValueError("syntax error")
        
    total = words[0]
    for i in range(1, len(words), 2):
        operation = known_operations[words[i]]
        total = operation(total, words[i + 1])

    return total
