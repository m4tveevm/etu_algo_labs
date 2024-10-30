from algo.Stack import Stack


def calculate_minrun(n):
    count = 0
    while n >= 64:
        count |= n & 1
        n >>= 1
    return n + count


def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item


def binary_search(arr, key, start):
    left = start
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid
    return left


def merge(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]
    i = j = k = 0
    gallop_trigger = 7
    count = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[start + k] = left[i]
            i += 1
        else:
            arr[start + k] = right[j]
            j += 1
        k += 1
        count += 1

        if count >= gallop_trigger:
            if left[i] <= right[j]:
                idx = binary_search(right, left[i], j)
                arr[start + k : start + k + idx - j] = right[j:idx]
                k += idx - j
                j = idx
            else:
                idx = binary_search(left, right[j], i)
                arr[start + k : start + k + idx - i] = left[i:idx]
                k += idx - i
                i = idx
    while i < len(left):
        arr[start + k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[start + k] = right[j]
        j += 1
        k += 1


def find_runs(arr, minrun):
    n = len(arr)
    runs = []
    i = 0

    while i < n:
        run_start = i
        run_end = i + 1
        if run_end < n and arr[run_end] < arr[run_start]:
            while run_end < n and arr[run_end] < arr[run_end - 1]:
                run_end += 1
            arr[run_start:run_end] = arr[run_start:run_end][::-1]
        else:
            while run_end < n and arr[run_end] >= arr[run_end - 1]:
                run_end += 1

        run_length = run_end - run_start
        if run_length < minrun:
            run_end = min(n, run_start + minrun)
            insertion_sort(arr, run_start, run_end - 1)

        runs.append((run_start, run_end))
        i = run_end

    return runs


def timsort(arr):
    n = len(arr)
    minrun = calculate_minrun(n)
    runs = find_runs(arr, minrun)

    stack = Stack()
    for run in runs:
        stack.push(run)
        while len(stack) > 1:
            run_b = stack.pop()
            run_a = stack.pop()
            if run_a[1] - run_a[0] <= run_b[1] - run_b[0]:
                merge(arr, run_a[0], run_b[0], run_b[1])
                stack.push((run_a[0], run_b[1]))
            else:
                stack.push(run_a)
                stack.push(run_b)
                break
