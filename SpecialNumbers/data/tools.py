""" Set of tools """


def quit_():
    """ Bye bye. """
    raise SystemExit


def display(result, prompt):
    print('{0}\n{1}\n{2}\n{0}'.format('=' * 30, prompt, result))


def display_menu(options: dict) -> None:
    """ Nice menu display. """
    print("AVAILABLE OPTIONS:\n(type Quit to quit)")
    new_line = 1
    for item in options.keys():
        end_char = '\t'
        if new_line % 3 == 0:
            end_char = '\n'
        print("- {:15}".format(item), end=end_char)
        new_line += 1
    else:  # to add a new line at the end in case the options available are multiple of three
        if new_line % 3 == 0:
            print()


def get_option(options: dict):
    """ Given a dictionary of possible options, user picks one. """
    display_menu(options)
    while True:
        option = input("\nChoose: ").title()
        if option in options.keys():
            return option
        elif option == 'Quit':
            quit_()
        else:
            print("Not available, yet.")


def get_integer(prompt=''):
    """ Asks to input a positive integer (therefore excludes 0). """
    while True:
        integer = input(prompt)
        if integer.isdigit() and integer != '0':
            integer = int(integer)
            return integer
        else:
            print("Invalid number, must be a positive integer.")
