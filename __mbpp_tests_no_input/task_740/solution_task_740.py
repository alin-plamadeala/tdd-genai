def tuple_to_dict(tpl):
    if len(tpl) % 2 != 0:
        raise ValueError("Input tuple must have an even number of elements.")
    return {tpl[i]: tpl[i + 1] for i in range(0, len(tpl), 2)}
