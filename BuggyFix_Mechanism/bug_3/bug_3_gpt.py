def bucketsort(arr):
    if len(arr) == 0:
        return []

    max_val = max(arr)
    min_val = min(arr)
    if max_val == min_val:
        return arr.copy()  # All elements are the same

    # Adjust size to avoid division by zero and spread values properly
    size = (max_val - min_val) / len(arr) + 1e-9

    buckets = [[] for _ in range(len(arr))]

    for i in range(len(arr)):
        j = int((arr[i] - min_val) / size)
        if j >= len(arr):
            j = len(arr) - 1
        buckets[j].append(arr[i])

    for i in range(len(arr)):
        buckets[i] = sorted(buckets[i])

    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result