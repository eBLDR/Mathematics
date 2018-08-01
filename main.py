""" Main file """

import tools
import specialnumbers as num
import specialseries as ser
import matrixes as matr


def main():
    while True:
        current_mode = tools.get_option(modes_available)
        modes_available[current_mode]()
        input("Press <return> to continue.")


modes_available = {'Special Series': ser.main,
                   'Special Numbers': num.main,
                   'Matrices': matr.main}


if __name__ == '__main__':
    main()
