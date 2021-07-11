# PyPI: https://pypi.org/
# The Python Package Index (PyPI) is a repository of software for the Python programming language.
# PyPI helps you find and install software developed and shared by the Python community.

# PrettyTable: https://pypi.org/project/prettytable/

# Install packages in Pycharm:
# https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html#interpreter-settings

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)

