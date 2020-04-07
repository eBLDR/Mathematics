import math


def max_value(data_set: list) -> (int, float):
    """
    Calculates the maximum value.
    """
    return max(data_set)


def min_value(data_set: list) -> (int, float):
    """
    Calculates the minimum value.
    """
    return min(data_set)


def range_(data_set: list) -> (int, float):
    """
    Calculates the range, highest value - lowest value.
    """
    return max(data_set) - min(data_set)


def mean(data_set: list) -> (int, float):
    """
    Calculates the arithmetic mean, the average.
    """
    return sum(data_set) / len(data_set)


def median(data_set: list) -> (int, float):
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


def variance(data_set: list) -> (int, float):
    """
    Calculates the variance, the mean of the squared difference from each value to the mean.
    """
    mean_ = mean(data_set)
    result = mean([(mean_ - n) ** 2 for n in data_set])
    return result


def standard_deviation(data_set: list) -> (int, float):
    """
    Calculates standard deviation, how far apart all the numbers are in a set.
    """
    return math.sqrt(variance(data_set))


def higher_median(data_set: list) -> (int, float):
    """
    Calculates the higher median, the median of the subset of the 50% higher numbers.
    """
    data_set.sort()
    num_of_items = len(data_set)
    if num_of_items % 2 == 0:
        return median(data_set[int(num_of_items / 2):])
    else:
        return median(data_set[int(num_of_items / 2) + 1:])


def lower_median(data_set: list) -> (int, float):
    """
    Calculates the lower median, the median of the subset of the 50% lower numbers.
    """
    data_set.sort()
    return median(data_set[:int(len(data_set) / 2)])


def interquartile_range(data_set: list) -> (int, float):
    """
    Calculates the interquartile range (IQR), the difference between higher and lower median.
    """
    return higher_median(data_set) - lower_median(data_set)


if __name__ == '__main__':
    """
    Run all callable objects in module.
    :param data_set: data set to be assessed
    """
    sample = [100, 98, 105, 90, 102, 110, 102]

    for name, method in [(name_, method_) for name_, method_ in locals().items() if callable(method_)]:
        print('{}: {}'.format(name.upper(), method(sample)))
