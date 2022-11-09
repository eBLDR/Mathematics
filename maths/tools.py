""" A set of tools. """


def quit_():
    """ Bye bye. """
    raise SystemExit


def display(result, prompt):
    if isinstance(result, dict):
        result = "\n".join(
            [
                f"{attr}: {value}" for attr, value in result.items()
            ]
        )

    print(f"{'=' * 30}\n{prompt}\n\n{result}\n{'=' * 30}")


def display_menu(options: dict) -> None:
    """ Nice menu display. """
    print("AVAILABLE OPTIONS:\n(type Quit to quit)")
    new_line = 1
    for item in options.keys():
        end_char = "\t"
        if new_line % 3 == 0:
            end_char = "\n"
        print(f"- {item:15}", end=end_char)
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

        elif option == "Quit":
            quit_()

        print("Not available, yet.")


def get_integer(prompt=''):
    """ Asks to input a positive integer [1, 2, 3, ...). """
    while True:
        integer = input(prompt)
        if integer.isdigit() and integer != "0":
            return int(integer)
        else:
            print("Invalid number, must be a positive integer.")
