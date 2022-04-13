# allthethings

Various utilities augmenting the python standard library.

## `base_convert`

```
base_convert(s, from_base: int, to_base: int, alphabet="0123456789abcdefghijklmnopqrstuvwxyz") -> str
```

## class `DateRange`

...

## `at_end_of_month`

```
at_end_of_month(d: date) -> date
```

Returns a date at the end of the month of the given date.

```
at_end_of_month(read_date('2022-02-03')) --> '2020-02-28'
at_end_of_month(read_date('2020-02-03')) --> '2020-02-29'
```

## `read_date`

```
read_date(value: Union[date, str]) -> date
```

## `make_dsn`

```
make_dsn(protocol: str, *, host: str, port: int, database: str, username: str, password: str) -> str
```

### `make_postgres_dsn`

```
make_postgres_dsn(*, host: str, database: str, username: str, password: str, port: int = 5432) -> str
```

## `grouper`

```
grouper(iterable: Iterable[U], n) -> Iterator[List[U]]
```

## `groupby`

```
groupby(f: Callable[[U], R], xs: Iterable[U]) -> Dict[R, List[U]]
```

like Scala's groupby, unlike Haskell's/Python's groupby

## `dedup`

```
dedup(xs: Iterable[U], on=lambda x: x) -> Iterator[U]
```

## `range_incl`

```
range_incl(lower: E, upper: E, step: Optional[Union[Callable[[E], E], Number]] = None) -> Iterator[E]

with E = TypeVar('E', Number, date, covariant=True)
```

## `range_excl`

```
range_excl(lower: E, upper: E, step: Optional[Union[Callable[[E], E], Number]] = None) -> Iterator[E]

with E = TypeVar('E', Number, date, covariant=True)
```

## class `Stopwatch`

...
