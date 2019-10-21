"""
Simple script with x as a only positional command line argument.
Prints the result of calculations with x.

Edit a function(argument) to change the logic.
"""

import argparse

parser = argparse.ArgumentParser(description='Process an argument and return a result')
parser.add_argument('argument',
                    metavar='x',
                    type=float,
                    help='a float argument for script')


def function(argument: float):
    """
    Function that makes any calculations on argument.
    Edit this function to change the logic of the script.

    :param argument: only argument that function takes
    :return: result of calculations on argument
    """
    return argument * 42


if __name__ == '__main__':
    args = parser.parse_args()
    x = args.argument

    # complex calculations
    result = function(x)
    print(f'Result of x * 42 = {result}')
