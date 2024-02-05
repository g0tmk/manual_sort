"""
This program helps you sort a list of items. It reads a list of items from a
text file and asks the user to compare each pair of items to determine the
order. The sorted list is then printed to the console.
"""

import argparse
from pick import pick

_PROGRAM_NAME = "manual_sort"
_VERSION = "0.0.1"


class ItemToSort:
    """An item to be sorted. Contains a lt method that asks the user which item is greater."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __lt__(self, other):
        # ask the user which item is greater
        _, index = pick(
            [str(self), str(other)],
            "Which item is greater?",
        )
        return index == 1


def main():
    """Accept a file via cli and ask a series of questions to sort the list."""
    parser = argparse.ArgumentParser(description="Help you sort a list of items")
    parser.add_argument(
        "file", help="Text file containing the list of items to be sorted"
    )
    parser.add_argument(
        "--version", action="version", version=f"{_PROGRAM_NAME} {_VERSION}"
    )
    args = parser.parse_args()

    # read each line from the file and create a list of ItemToSort objects
    items = []
    with open(args.file, encoding="utf-8") as file:
        for line in file:
            if line.strip():
                items.append(ItemToSort(line.strip()))

    # sort the list
    items.sort()

    # print the sorted list
    for item in items:
        print(item)


if __name__ == "__main__":
    main()
