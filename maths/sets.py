def cardinality(set_):
    c = 0
    for _ in set_:
        c += 1

    return c


def membership(element, set_):
    for e in set_:
        if e == element:
            return True

    return False


def are_equal(set_a, set_b):
    return is_subset(set_a, set_b) and is_subset(set_b, set_a)


def is_subset(set_a, set_b):
    for e in set_a:
        if not membership(e, set_b):
            return False

    return True


def are_disjoint(set_a, set_b):
    for e in set_a:
        if membership(e, set_b):
            return False

    return True


def union(set_a, set_b):
    u = set()
    for e in set_a:
        u.add(e)

    for e in set_b:
        if not membership(e, u):
            u.add(e)

    return u


def intersection(set_a, set_b):
    i = set()
    for e in set_a:
        if membership(e, set_b):
            i.add(e)

    return i


def difference(set_a, set_b):
    d = set()
    for e in set_a:
        if not membership(e, set_b):
            d.add(e)

    return d


def symmetric_difference(set_a, set_b):
    return union(
        difference(set_a, set_b),
        difference(set_b, set_a),
    )
