import random
def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x-1] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i+1] * counts[i])

    return sorted_arr


def test_bucketsort():
    # Test empty array
    arr = []
    k = 5
    assert bucketsort(arr, k) == []

    # Test array with one element
    arr = [3]
    k = 5
    assert bucketsort(arr, k) == [3]

    # Test sorted array
    arr = [1, 2, 3, 4, 5]
    k = 5
    assert bucketsort(arr, k) == [1, 2, 3, 4, 5]

    # Test reverse-sorted array
    arr = [5, 4, 3, 2, 1]
    k = 5
    assert bucketsort(arr, k) == [1, 2, 3, 4, 5]

    # Test array with duplicates
    arr = [3, 1, 5, 2, 5, 4, 1, 3]
    k = 5
    assert bucketsort(arr, k) == [1, 1, 2, 3, 3, 4, 5, 5]

    # Test array with all elements the same
    arr = [4, 4, 4, 4, 4]
    k = 5
    assert bucketsort(arr, k) == [4, 4, 4, 4, 4]

    # Test array with large k
    arr = [10, 5, 1, 3, 8, 2, 7, 9, 6, 4]
    k = 10
    assert bucketsort(arr, k) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # # Test array with negative numbers
    # arr = [-3, 2, 5, -1, 0, 2, -4]
    # k = 5
    # assert bucketsort(arr, k) == [-4, -3, -1, 0, 2, 2, 5]

    # Test random arrays
    for i in range(10):
        arr = [random.randint(1, 100) for _ in range(100)]
        k = 100
        assert bucketsort(arr, k) == sorted(arr)


if __name__ == "__main__":
    test_bucketsort()
    print("All tests passed")