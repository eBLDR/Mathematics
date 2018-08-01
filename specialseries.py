"""
A collection of different interesting sequences from recreational numbers theory.
Series are dependent on the other numbers in the series.
"""
import tools


def display(result, prompt):
    print("{0}\n{1}\n{2}\n{0}".format("="*30, prompt, result))


def fibonacci_series(elements=0) -> list:
    """ n = n-1 + n-2"""
    seq = [0, 1]
    for i in range(elements - len(seq)):
        seq.append(seq[i] + seq[i + 1])
    return seq


def padovan_series(elements=0) -> list:
    """ n = n-2 + n-3 """
    seq = [0, 1, 1]
    for i in range(elements - len(seq)):
        seq.append(seq[i] + seq[i + 1])
    return seq


def main():
    series = tools.get_option(series_available)
    elements = tools.get_integer("Number of elements: ")
    result = series_available[series](elements)
    prompt = "{} sequence with the {} first elements:".format(series, elements)
    display(result, prompt)


series_available = {'Fibonacci': fibonacci_series,
                    'Padovan': padovan_series}
