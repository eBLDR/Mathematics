"""
A collection of different interesting number's properties from recreational numbers theory.
A property is inherent of the number.
"""
# ALL THE ROUND() ARE DUE TO FLOATING ARITHMETIC ISSUES
import tools


def display(result, prompt):
    print("{0}\n{1}\n{2}\n{0}".format("="*30, prompt, result))


def check_attributes_init():
    """ Collects needed data """
    number = tools.get_integer("Number to be assessed: ")
    return check_attributes(number)


def check_attributes(number: int):
    attributes = {}
    for attr in attributes_available:
        value = attributes_available[attr](number)
        if value is None:
            value = False
        attributes[attr] = value
    prompt = "Attributes of number {}:".format(number)
    return attributes, prompt


def series_constructor_init():
    """ Collects needed data """
    attribute = tools.get_option(attributes_available)
    elements = tools.get_integer("Number of elements: ")
    return series_constructor(attribute, elements)


def series_constructor(check, elements=0):
    """ Construct a sequence with a given number property """
    seq = []
    i = 1
    while len(seq) < elements:
        if attributes_available[check](i):
            seq.append(i)
        i += 1
    prompt = "{} sequence with the {} first elements:".format(check, elements)
    return seq, prompt


def proper_divisors(number: int) -> list:
    """ Returns a list with the proper divisors of a given number. """
    proper_div = []
    for i in range(1, number):  # finding the proper divisors
        if number % i == 0:
            proper_div.append(i)

    return proper_div


def aliquot_sum(number: int) -> int:
    """ The sum of the proper divisors. """
    prop_div = proper_divisors(number)
    ali_sum = 0
    for i in prop_div:
        ali_sum += i

    return ali_sum


def prime_factors(number: int) -> list:
    """ Returns the prime factors. """
    prime_fact = []
    left = number
    while left:  # finding the prime factors
        for i in range(2, left + 1):
            if left % i == 0:
                prime_fact.append(i)
                left = int(left / i)  # left /= i will lead to a type change from int to float
                break
        else:
            break

    return prime_fact


def sum_of_digits(number: int) -> int:
    """ Returns the sum of the digits of number. """
    sum_dig = 0
    for i in str(number):
        sum_dig += int(i)

    return sum_dig


def is_prime(number: int) -> bool:
    """ Proper divisors include only 1. """
    prop_div = proper_divisors(number)
    return True if len(prop_div) == 1 else False


def is_square(number: int) -> bool:
    """ Perfect square n**2. """
    n = round(number ** (1/2), 5)
    return True if number % n == 0 else False


def is_cube(number: int) -> bool:
    """ Perfect cube n**3. """
    n = round(number ** (1/3), 5)
    return True if number % n == 0 else False


def is_perfect(number: int) -> bool:
    """ The sum of its proper divisors is equal to the number itself. """
    ali_sum = aliquot_sum(number)
    return True if ali_sum == number else False


def is_abundant(number: int) -> bool:
    """ The sum of its proper divisors is greater than the number itself.
    A number with the opposite property is called 'deficient'. """
    ali_sum = aliquot_sum(number)
    return True if ali_sum > number else False


def is_happy(number: int) -> bool:
    """ Replaces the number with the sum of the squares of its digits, if the process
    finishes reaching 1, the number is happy. Otherwise is a sad number. """
    attempts = 15
    while attempts > 0:
        next_number = 0
        for digit in str(number):
            next_number += int(digit) ** 2
        number = next_number
        if number == 1:
            return True
        attempts -= 1
    else:
        return False


def is_powerful(number: int) -> bool:
    # LONG COMPUTING TIME
    """ Can be defined as the product of a square and a cube. """
    for i in range(1, number + 1):
        for j in range(1, number + 1):
            if (i**2) * (j**3) == number:
                return True
    else:
        return False


def is_palindromic(number: int) -> bool:
    """ A symmetric number """
    return True if str(number) == str(number)[::-1] else False


def is_magic(number: int) -> bool:
    """ Magic (or polydivisible) number, with given digits abcde... meets:
    a is not 0, ab is multiple of 2, abc is multiple of 3, and so on. """
    for i in range(1, len(str(number)) + 1):
        if int(str(number)[0: i]) % i != 0:
            return False
    else:
        return True


def is_harmonic(number: int) -> bool:
    """ Harmonic divisor number (or Ore number) is a number which its harmonic mean is an integer. """
    divisors = proper_divisors(number)
    divisors.append(number)  # ! divisors include proper divisors + itself!
    dividend = len(divisors)
    divisor = 0
    for j in divisors:
        divisor += 1/j
    return True if round(dividend % divisor, 5) == 0 else False


def is_sphenic(number: int) -> bool:
    """ Positive integer that is the product of three distinctive prime numbers. """
    prime_fact = prime_factors(number)
    if len(prime_fact) == 3:  # first condition, must have 3 elements
        for factor in prime_fact:
            times = 0
            for duplicate in prime_fact:
                if factor == duplicate:
                    times += 1
            if times >= 2:  # second condition, no repeated elements
                return False
        else:
            return True


def is_smith(number: int) -> bool:
    """ Is a composite number which the sum of its digits is equal to the sum
    of the digits of its prime factors. """
    if not is_prime(number):
        prime_fact = prime_factors(number)
        sum_dig_fact = 0
        for i in prime_fact:
            sum_dig_fact += sum_of_digits(i)

        sum_dig = sum_of_digits(number)

        return True if sum_dig_fact == sum_dig else False


def is_harshad(number: int) -> bool:
    """ (aka Niven) It's divisible by the sum of its digits. """
    sum_dig = sum_of_digits(number)
    return True if number % sum_dig == 0 else False


def is_antiprime(number: int) -> bool:
    """ (aka Highly Composite) It's a positive integer with more divisors than any smaller integer. """
    prop_div = proper_divisors(number)
    prop_div.append(number)

    for i in range(1, number):
        i_prop_div = proper_divisors(i)
        i_prop_div.append(i)
        if len(i_prop_div) >= len(prop_div):
            return False
    else:
        return True


# TODO: NEEDS WORK
"""
def is_practical(number: int) -> bool:
    # All it's smaller integers can be expressed as the sum of distinct proper divisors of itself.
    prop_div = proper_divisors(number)
    sums_of_all_possible_combinations = []
    for i in range(len(prop_div)):
        for j in range(i, len(prop_div)):
            print(i, j)
            sums_of_all_possible_combinations.append(sum(prop_div[i:j+1]))
            print("slice is ", prop_div[i:j+1])
            print("list is ", sums_of_all_possible_combinations)
"""


def main():
    option = tools.get_option(options_available)
    result, prompt = options_available[option]()
    display(result, prompt)


options_available = {'Attributes': check_attributes_init,
                     'Sequences': series_constructor_init}

attributes_available = {'Prime': is_prime,
                        'Square': is_square,
                        'Cube': is_cube,
                        'Perfect': is_perfect,
                        'Abundant': is_abundant,
                        'Happy': is_happy,
                        'Powerful': is_powerful,
                        'Palindromic': is_palindromic,
                        'Magic': is_magic,
                        'Harmonic': is_harmonic,
                        'Sphenic': is_sphenic,
                        'Smith': is_smith,
                        'Harshad': is_harshad,
                        'Antiprime': is_antiprime}#,
                        #'Practical': is_practical}

# For testing only
if __name__ == '__main__':
    print(is_prime(22))
