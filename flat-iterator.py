import itertools

class FlatIterator():
    def __init__(self, value):
        self.value = value
        self.flat = list(itertools.chain.from_iterable(self.value))
        self.cursor = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.flat) + 1:
            raise StopIteration
        
        return self.flat[self.cursor - 1]    
    

if __name__ == '__main__':
    
    single_nested = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
    ]
    
    unnested = FlatIterator(single_nested)
    
    # result checking:
    
    # for i in unnested:
    #     print(i)
        
    # flat_list = [item for item in FlatIterator(single_nested)]
    # print(flat_list)
    
    print(next(unnested))
    print(next(unnested))
    print(next(unnested))
    print(next(unnested))
    print(next(unnested))
    print(next(unnested))
    print(next(unnested))
    print(next(unnested))
    print(next(unnested))
    print(next(unnested))
    print(next(unnested))
    print(next(unnested))