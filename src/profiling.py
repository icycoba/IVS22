"""
Soubor:     profiling.py
Autor:      Petra Dudová    (xdudov02)
            Martin Hlinský  (xhlins01)
Projekt:    IVS #2 - Tvorba kalkulačky
Popis:      Program pro výpočet výběrové směrodatné odchylky
"""

import sys
# import cProfile
# import pstats

from expression_to_num import MathSolver, MathOperations


def mean(narray):
    # xmean = 1/N * sum(x_i)
    result = MathOperations()
    for num in narray:
        result.add(num)
    result.div(len(narray))
    return result.getvalue()


def deviationsum(narray):
    # sum(x_i^2)
    result = MathOperations()
    for num in narray:
        tempnum = MathOperations(num)
        tempnum.pow(2)
        result.add(tempnum.getvalue())
    return result.getvalue()


def deviation(narray):
    # sqrt(1/N-1 * (sum(x_i^2) - N * x_mean^2))
    result = MathOperations()
    x_mean = mean(narray)
    s_sum = deviationsum(narray)

    nxmeansquared = float(MathSolver().solve(f"{len(narray)}*{x_mean}^2"))
    arraylen = float(MathSolver().solve(f"{len(narray)}-1"))

    result.add(s_sum)
    result.sub(nxmeansquared)
    result.div(arraylen)
    result.root(2)
    return result.getvalue()


if __name__ == "__main__":
    # profiler = cProfile.Profile()
    try:
        numarray = sys.stdin.read()
    except FileNotFoundError:
        print("Soubor nenalezen.", file=sys.stderr)
        exit(2)
    except Exception as e:
        print(f"Nastala neočekávaná chyba při otevírání souboru: \n{e}", file=sys.stderr)
        exit(3)
    numarray = numarray.split()
    try:
        numarray = list(map(int, numarray))
    except ValueError as e:
        print("ValueError: Jedna z hodnot nelze převést na číslo.", file=sys.stderr)
        exit(1)

    # profiler.run('deviation(numarray)')
    # p = pstats.Stats(profiler)
    # p.strip_dirs().sort_stats(SortKey.TIME).print_stats(10)

    s = deviation(numarray)
    print(s)
