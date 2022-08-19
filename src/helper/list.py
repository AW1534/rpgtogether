from collections import Counter


def contains_items(list, contains):
    i = -1
    for item in contains:
        i += 1
        try:
            list[i]
        except ValueError:
            return False

    return True


def sort(list):
    c = Counter(list)

    dict = {}

    for i in list:
        dict[i] = c[i]

    return dict


def sort_to_string(list, count_if_single=True):
    l = []
    cnt = sort(list)
    print(list)
    i = -1
    for item in cnt:
        i += 1
        l.append(f"{list[i]}\t(x{cnt[item]})")

    return l
