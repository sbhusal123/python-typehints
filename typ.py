from typing import Iterator, Iterable, Tuple, List, Generator

"""
- Iterator is an object, which one can iterate over. __next__()
- Iterable is an object, anything usable in "for" tuple, list, set
"""

# x: Iterator[int] = iter([1, 2, 3]) # <class 'tuple_iterator'>

x: Iterator[int] = iter((1, 2, 3)) # <class 'tuple_iterator'>

p: Iterator[Tuple] = iter( ((1, 2, 3), (4, 5, 6)) ) # <class 'tuple_iterator'>

# accessing data items in iterator
# print(next(p))
# print(next(p))

y: Iterable[int] = range(1, 10)
z: Iterable[int] = [1, 2, 3, 4]

q: Iterator[Tuple[int, Iterable[str]]] = iter(
    ((1, ("a", "b", "c")),
    (2, ("a", "b", "c")))
)

def natural_generator(lower_bnd: int, upper_bnd: int) -> Generator:
    for i in range(lower_bnd, upper_bnd):
        yield i


gen = natural_generator(1, 3)
print(next(gen))
print(next(gen))
# print(next(gen))