def max_value(data_set: list) -> int:
    """
    Calculates the maximum value.
    """
    return max(data_set)


def min_value(data_set: list) -> int:
    """
    Calculates the minimum value.
    """
    return min(data_set)


def range_(data_set: list) -> int:
    """
    Calculates the range, highest value - lowest value.
    """
    return max(data_set) - min(data_set)


def mean(data_set: list) -> int:
    """
    Calculates the arithmetic mean, the average.
    """
    return sum(data_set) / len(data_set)


def median(data_set: list) -> int:
    """
    Calculates the median, the central values of a sorted set.
    """
    data_set.sort()
    num_of_items = len(data_set)
    mid_index = int(num_of_items / 2)
    if num_of_items % 2 == 0:
        return (data_set[mid_index] + data_set[mid_index - 1]) / 2
    else:
        return data_set[mid_index]


def mode(data_set: list) -> list:
    """
    Calculates the mode, the value that appears the most.
    """
    mode_mapper = {}
    for value in data_set:
        mode_mapper.setdefault(value, 0)
        mode_mapper[value] += 1

    sorted_by_value = sorted(mode_mapper.items(), key=lambda kv: (kv[1], kv[0]))
    max_repetitions = sorted_by_value[-1][1]
    result = []

    # No mode, all values are unique
    if max_repetitions == 1:
        return result

    for m in range(len(sorted_by_value) - 1, 0, -1):
        if sorted_by_value[m][1] != max_repetitions:
            break
        result.append(sorted_by_value[m][0])

    return result


s = [100, 98, 105, 90, 102, 90, 110]
print(mean(s))
print(median(s))

print(mode(s))
