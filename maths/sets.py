"""
Avoiding to use Python in-built methods for sets.
"""


def cardinality(set_):
    """
    Equivalent to:
    return len(set_)
    """
    c = 0
    for _ in set_:
        c += 1

    return c


def membership(element, set_):
    """
    Equivalent to:
    return element in set_
    """
    for e in set_:
        if e == element:
            return True

    return False


def are_equal(set_a, set_b):
    """
    Equivalent to:
    return set_a == set_b
    """
    return is_subset(set_a, set_b) and is_subset(set_b, set_a)


def is_subset(set_a, set_b):
    """
    Equivalent to:
    return set_a <= set_b
    """
    for e in set_a:
        if not membership(e, set_b):
            return False

    return True


def is_superset(set_a, set_b):
    """
    Equivalent to:
    return set_a >= set_b
    """
    return is_subset(set_b, set_a)


def is_proper_subset(set_a, set_b):
    """
    Equivalent to:
    return set_a < set_b
    """
    if not is_subset(set_a, set_b):
        return False

    for e in set_b:
        if not membership(e, set_a):
            return True

    return False


def is_proper_superset(set_a, set_b):
    """
    Equivalent to:
    return set_a > set_b
    """
    if not is_superset(set_a, set_b):
        return False

    for e in set_b:
        if not membership(e, set_a):
            return True

    return False


def union(set_a, set_b):
    """
    Equivalent to:
    return set_a | set_b
    """
    u = set()
    for e in set_a:
        u.add(e)

    for e in set_b:
        if not membership(e, u):
            u.add(e)

    return u


def intersection(set_a, set_b):
    """
    Equivalent to:
    return set_a & set_b
    """
    i = set()
    for e in set_a:
        if membership(e, set_b):
            i.add(e)

    return i


def are_disjoint(set_a, set_b):
    """
    Equivalent to:
    return len(intersection(set_a, set_b)) == 0
    """
    for e in set_a:
        if membership(e, set_b):
            return False

    return True


def difference(set_a, set_b):
    """
    Equivalent to:
    return set_a - set_b
    """
    d = set()
    for e in set_a:
        if not membership(e, set_b):
            d.add(e)

    return d


def symmetric_difference(set_a, set_b):
    """
    Equivalent to:
    return set_a ^ set_b
    """
    return union(
        difference(set_a, set_b),
        difference(set_b, set_a),
    )


def cartesian_product(set_a, set_b):
    return {(a, b) for a in set_a for b in set_b}
