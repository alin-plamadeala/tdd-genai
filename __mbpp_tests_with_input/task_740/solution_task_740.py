def tuple_to_dict(tpl):
    return {tpl[i]: tpl[i + 1] for i in range(0, len(tpl), 2)}