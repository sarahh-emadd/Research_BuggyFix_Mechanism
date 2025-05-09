#bug_3 fixed github
def bucketsort(arr):
    max_val = max(arr)
    size = max_val / len(arr) if max_val != 0 else 1
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
