"""
Soubor:     profiling.py
Autor:      Petra Dudová    (xdudov02)
            Martin Hlinský  (xhlins01)
Projekt:    IVS #2 - Tvorba kalkulačky
Popis:      Program pro výpočet výběrové směrodatné odchylky
"""

from expression_to_num import MathSolver
import sys


def mean(numarray):
    result = 0
    for num in numarray:
        result += num
    result /= len(numarray)
    return result


if __name__ == "__main__":
    # Ošetřit správné otevření souboru
    numarray = sys.stdin.read()
    numarray = numarray.split()
    try:
        numarray = list(map(int, numarray))
    except ValueError as e:
        print(f"ValueError: Jedna z hodnot nelze převést na číslo.")

    print(numarray)

# ...
