from typing import TypeVar, Dict, List, Iterable, Callable, Iterator

U = TypeVar('U')
R = TypeVar('R')


def groupby(f: Callable[[U], R], xs: Iterable[U]) -> Dict[R, List[U]]:
    r = dict()
    for x in xs:
        k = f(x)
        if k not in r:
            r[k] = []
        r[k].append(x)
    return r


def dedup(xs: Iterable[U]) -> Iterator[U]:
    """
    Deduplicates an iterable. Any item is guaranteed to only occur once in the result.
    """

    seen = set()
    for x in xs:
        if x in seen:
            continue
        seen.add(x)
        yield x
