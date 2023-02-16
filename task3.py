import types
from itertools import chain
from task2 import logger


@logger('task3.log')
def flat_generator(list_of_lists):
    items = list(chain(*list_of_lists))
    for item in items:
        yield item

@logger('task3.log')
def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    print(list(flat_generator(list_of_lists_1)))

if __name__ == '__main__':
    test_2()
