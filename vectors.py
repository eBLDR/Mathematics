""" A collection of vector operations and other properties. """


def check_length(*args):
    """True if all the vectors have the same length."""
    if args:
        length_of_vectors = [len(args[i]) for i in range(len(args))]
        ref = length_of_vectors[0]

        return all(ref == j for j in length_of_vectors)


def add_vectors(*args):
    """ Simple vector addition.
    r = (Ax + Bx, Ay + By, Az + Bz) """
    if check_length(*args):
        r = [0 for n in range(len(args[0]))]
        for vector in args:
            for k in range(len(vector)):
                r[k] += vector[k]

        return r


def scalar_product(v1, v2):
    """ Scalar product between 2 vectors.
    r = (AxBx + AyBy + AzBz) """
    if check_length(v1, v2):
        r = [a * b for a, b in zip(v1, v2)]

        return r


ve1 = [0, 5, 4]
ve2 = [-1, 2, 6]
ve3 = [4, -7, 0]

print(add_vectors(ve1, ve2, ve3))
print(scalar_product(ve1, ve2))
