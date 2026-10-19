def merge_dicts_with_overlapping_keys(dicts):
    result = {}

    for d in dicts:
        for key, value in d.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value

    return result