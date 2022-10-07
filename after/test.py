from typing import List


def find_mode(numbers: list) -> tuple:
    result = None
    if len(numbers) <= 0:
        return result
    num_count = {(x, numbers.count(x)) for x in numbers}
    num_count = list(num_count)
    num_count.sort(key=lambda x: x[1])
    result = num_count[-1]
    return result


def test_mode():
    expected = find_mode([1, 2, 3, 4, 4, 5, 5, 4, 4])
    actual = (4, 4)
    assert expected == actual


def test_mode_empty_list():
    result = find_mode([])
    assert result is None


