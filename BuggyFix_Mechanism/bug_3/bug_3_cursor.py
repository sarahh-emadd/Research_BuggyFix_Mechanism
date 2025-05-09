#bug_fix3

def bucketsort(arr):
    if not arr:
        return arr
        
    max_val = max(arr)
    min_val = min(arr)
    size = (max_val - min_val) / len(arr)
    
    if size == 0:
        return arr
        
    buckets = [[] for _ in range(len(arr) + 1)]

    for num in arr:
        j = int((num - min_val) / size)
        if j >= len(buckets):
            buckets[-1].append(num)
        else:
            buckets[j].append(num)

    result = []
    for bucket in buckets:
        if bucket:
            bucket.sort()
            result.extend(bucket)

    return result
