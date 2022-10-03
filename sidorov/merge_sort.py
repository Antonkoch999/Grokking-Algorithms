
def merge(a, b):
    merged_list = []
    i, j, len_a, len_b = 0, 0, len(a), len(b)
    while i < len_a or j < len_b:
        if a[i] <= b[j]:
            merged_list.append(a[i])
            i += 1
        else:
            merged_list.append(b[j])
            j += 1
        if i == len_a:
            merged_list.extend(b[j:])
            j = len_b
        if j == len_b:
            merged_list.extend(a[i:])
            i = len_a
    return merged_list


def merge_sort(a):
    if len(a) > 1:
        m = len(a) // 2
        return merge(merge_sort(a[0:m]), merge_sort(a[m:]))
    else:
        return a[:]


print(merge_sort([7, 3, 9, 6, 1, 4, 0, 2, 5, 0]))
