def generator():
    try:
        yield 1
    except Exception as e:
        if e.args == (1, ):
            yield 42
        elif e.args == (3, ):
            yield 24
        else:
            yield 21
    else:
        yield 1
