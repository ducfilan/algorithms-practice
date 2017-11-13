def pair_sum(arr, k):
    count = 0
    trace = {}

    for e in arr:
        if e in trace:
            count += 1
        else:
            trace[k - e] = 0

    return count