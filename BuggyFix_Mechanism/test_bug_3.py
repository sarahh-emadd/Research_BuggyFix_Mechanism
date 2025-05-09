def bucketsort(arr):
    max_val = max(arr)
    size = max_val / len(arr)
    buckets = [[] for _ in range(len(arr))]

    for i in range(len(arr)):
        j = int(arr[i] / size)
        if j != len(arr):
            buckets[j].append(arr[i])
        else:
            buckets[len(arr) - 1].append(arr[i])

    for i in range(len(arr)):
        buckets[i] = sorted(buckets[i])

    result = []
    for i in range(len(arr)):
        result = result + buckets[i]

    return result


# ✅ Test cases
def test_bucketsort():
    tests = [
        ([4, 2, 3, 1], [1, 2, 3, 4]),
        ([0.42, 0.32, 0.23, 0.52, 0.25, 0.47], sorted([0.42, 0.32, 0.23, 0.52, 0.25, 0.47])),
        ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ([0.91, 0.82, 0.73], sorted([0.91, 0.82, 0.73])),
        ([1], [1]),
    ]

    for idx, (inp, expected) in enumerate(tests):
        try:
            result = bucketsort(inp)
            assert result == expected, f"Test {idx + 1} failed: Expected {expected}, got {result}"
            print(f"Test {idx + 1} passed ✅")
        except Exception as e:
            print(f"Test {idx + 1} failed ❌: {str(e)}")

test_bucketsort()