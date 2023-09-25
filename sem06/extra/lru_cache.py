import functools


def cache(max_size):
    def wrapper(func):
        if max_size == 0:  # здесь мы не реализуем кеш, так как в аргументе нам задали, что кеш пустой
            @functools.wraps(func)
            def first_wraps(*args, **kwargs):
                return func(args, kwargs)
            return first_wraps

        used = dict()

        # в python все объект (https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)
        # object это базовый класс всех типов. Здесть я создаю объект, которым буду разделять позиционные аргументы
        # и именованные. Чуть ниже более подробное описание
        obj = object()

        @functools.wraps(func)
        def second_wraps(*args, **kwargs):
            # Идея не сложная. Для хранения будем использовать словарик.
            # Ключом у нас будет хэш от аргументов, но здесь нужно аккуратно:
            # - сначала храним позиционные аргументы
            # - разделяем их "dummy" (https://www.webopedia.com/definitions/dummy/) объектом
            # - после храним именованные аргументы в виде кортежа (ключ, значение)
            key = args + (obj, )
            for item in kwargs.items():
                key += item

            # Пользуемся встроенной хеш-функцией.
            # Кажется, что это необязательно и можно обойтись одним кортежом аргументов,
            # но у меня такое решение :)
            hash_key = hash(key)

            # Проверяем на то, если у нас этот подсчитанный хеш (то есть вызывали ли мы уже функцию от такой пачки аргументов).
            # В случае успеха, достаем хеш и перекладываем его в конец (напомню, что встроенный dict по-умолчанию является ordered
            # https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6)
            if hash_key in used:
                result = used[hash_key]
                del used[hash_key]
                used[hash_key] = result
                return result

            # В инном случае освобождаем наш словарик, если он полон
            if len(used) == max_size:
                _ = used.popitem(last=False)

            # Подсчитываем функцию и записываем в наш словарик
            result = func(*args, **kwargs)
            used[hash_key] = result

            return result

        return second_wraps

    return wrapper

