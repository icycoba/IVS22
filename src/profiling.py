"""
Soubor:     profiling.py
Autor:      Petra Dudová    (xdudov02)
            Martin Hlinský  (xhlins01)
Projekt:    IVS #2 - Tvorba kalkulačky
Popis:      Program pro výpočet výběrové směrodatné odchylky
"""

from expression_to_num import MathSolver, MathOperations
# from mathlib import MathOperations
import sys


def mean(narray):
    # xmean = 1/N * sum(x_i)
    result = MathOperations()
    for num in narray:
        result.add(num)
    result.div(len(narray))
    return result.getvalue()


def deviationsum(narray, xmean):
    result = MathOperations()
    nxmeansquared = float(MathSolver().solve(f"{len(narray)}*{xmean}^2"))
    arraylen = float(MathSolver().solve(f"{len(narray)}-1"))
    # print(nxmeansquared)
    for num in narray:
        tempnum = MathOperations(num)
        tempnum.pow(2)
        result.add(tempnum.getvalue())
    result.sub(nxmeansquared)
    result.div(arraylen)
    result.root(2)
    return result


def deviation(narray, xmean):
    # sqrt(1/N-1 * (sum(x_i^2 - N * x_mean^2)))
    pass


if __name__ == "__main__":
    # Ošetřit správné otevření souboru
    numarray = sys.stdin.read()
    numarray = numarray.split()
    try:
        numarray = list(map(int, numarray))
    except ValueError as e:
        print(f"ValueError: Jedna z hodnot nelze převést na číslo.")
        exit(1)

    x = mean(numarray)
    result = deviationsum(numarray, x)
    print(result.getvalue())

# ...
