import itertools

single_nested = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]

double_nested = [
    [['a', 'b', 'c'], ['d', 'e', 'f']],
    [['g', 'h', 'i'], ['j', 'k', 'l']],
    [[1, 2, 3], [4, 5, 6]]
]

# Generator for single nested objects

def generator_single_nested(iterable: list | tuple):
    '''Функция не может обрабатывать нессиметрично вложенные списки.'''
    
    try:
        flat_thing = tuple(itertools.chain.from_iterable(iterable))
        yield from flat_thing
    except Exception as ex:
        print('There is a non-symmetric nesting in the iterable!')

# result check
res = generator_single_nested(single_nested)
print(next(res))
print(next(res))
print(next(res))
print(next(res))

# Generator for many nested objects

def generator_many_nested(iterable: list | tuple):
    '''Функция по-прежнему не может обрабатывать нессиметрично вложенные списки.'''
    
    try:
        flat_thing = list(itertools.chain.from_iterable(iterable))
        if any(map(lambda x: type(x) == list, flat_thing)) is True:
            flat_thing = generator_many_nested(flat_thing)
        yield from flat_thing
    except Exception as ex:
        print('There is a non-symmetric nesting in the iterable!')

# result check   
res1 = generator_many_nested(double_nested)
print(next(res1))
print(next(res1))
print(list(res1))
