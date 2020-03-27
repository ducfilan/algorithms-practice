def solution(A):
    if not A:
        return -1

    sorted_A = sorted([(i, num)
                       for i, num in enumerate(A)], key=lambda t: t[1])
    max_distance = -1
    prev_i, curr_i = 0, 1
    N = len(A)

    while curr_i < N:
        if sorted_A[curr_i][1] == sorted_A[prev_i][1]:
            prev_i += 1
            curr_i += 1
            continue

        distance = abs(sorted_A[curr_i][0] - sorted_A[prev_i][0])
        max_distance = max(distance, max_distance)

        next_prev_i, next_curr_i = prev_i, curr_i

        if prev_i+1 < N and sorted_A[prev_i][1] != sorted_A[prev_i+1][1]:
            next_curr_i += 1

        if curr_i+1 < N and sorted_A[curr_i][1] != sorted_A[curr_i+1][1]:
            next_prev_i += 1

        prev_i, curr_i = next_prev_i, next_curr_i

    return max_distance
