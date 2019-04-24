""" Main file """
from SpecialNumbers.data import matrices
from SpecialNumbers.data import specialnumbers
from SpecialNumbers.data import specialseries
from SpecialNumbers.data import tools


def main():
    while True:
        current_mode = tools.get_option(modes_available)
        modes_available[current_mode]()
        input('Press <return> to continue.\n')


modes_available = {'Special Series': specialseries.main,
                   'Special Numbers': specialnumbers.main,
                   'Matrices': matrices.main}

if __name__ == '__main__':
    main()
