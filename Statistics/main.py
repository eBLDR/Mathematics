from Statistics.data import basic_statistics


def main(data_set):
    """
    Run all callable objects in module.
    :param data_set: data set to be assessed
    """
    for ref_name in dir(basic_statistics):
        attr = getattr(basic_statistics, ref_name)
        if callable(attr):
            result = attr(data_set)
            print('{}: {}'.format(ref_name.upper(), result))


if __name__ == '__main__':
    sample = [100, 98, 105, 90, 102, 110, 102]
    main(sample)
