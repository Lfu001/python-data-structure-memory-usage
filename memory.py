from memory_profiler import profile


@profile
def mem():
    a = list(range(1, 100001))
    x = map(lambda x: x**2, a)
    y = [i**2 for i in a]
    z = (i**2 for i in a)

    print(*map(type, (x, y, z)))


# <class 'map'> <class 'list'> <class 'generator'>

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#      4     44.4 MiB     44.4 MiB           1   @profile
#      5                                         def mem():
#      6     48.2 MiB      3.8 MiB           1       a = list(range(1, 100001))
#      7     48.2 MiB      0.0 MiB           1       x = map(lambda x: x**2, a)
#      8     52.1 MiB      3.9 MiB      100003       y = [i**2 for i in a]
#      9     52.1 MiB     -2.8 MiB           2       z = (i**2 for i in a)
#     10
#     11     52.1 MiB      0.0 MiB           1       print(*map(type, (x, y, z)))


if __name__ == "__main__":
    mem()
