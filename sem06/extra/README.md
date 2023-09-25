# LRU cache

Реализован декоратор **Least Recently Used (LRU) [Cache](https://ru.wikipedia.org/wiki/%D0%9A%D1%8D%D1%88)**. В аргументах декоратора указывается аргумент
`n` - в кеше сохраняются значения для `n` наборов аргументов функции, причем вытесняется из кеша сначала то, что использовалось давней всего.

Use case:
```python
# Будет сохранено 2048 наборов аргументов и ответов по этим аргументам функции Акермана.
# Вообще важно понимать, что функция должна быть детерминированная, в которой мы применяем кэш.
# В ином случае, это, кажется, что мы ожидаем не постоянный ответ от недетерминированной функции.

@cache(2048)
def ackermann(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackermann(m - 1, 1)
    if m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
    assert False, 'unreachable'


def main():
    print(f'{ackermann(1, 2)=}')


if __name__ == '__main__':
    main()
```

# Time it

Декоратор, который реализует подсчет последнего времени работы функции в секундах. Время лежит в поле `last_time_taken` функции, к которой применен декоратор.

Use case:
```python
@time_it
def ackermann(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackermann(m - 1, 1)
    if m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
    assert False, 'unreachable'


def main():
    print(f'{ackermann(1, 2)=}, {ackerman.last_time_taken=}')


if __name__ == '__main__':
    main()
```
