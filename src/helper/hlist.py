import random
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
        if count_if_single is True and cnt[item] == 1:
            l.append(f"{list[i]}\t")
        else:
            l.append(f"{list[i]}\t(x{cnt[item]})")

    return l

class Unique_generator:
    def __init__(self, list=None):
        if list is None:
            list = []
        self.list = list
        self.last_pick = []

    def pick(self, amt=1):
        curr_choice = self.last_pick
        while curr_choice is self.last_pick:
            curr_choice = []
            for i in range(amt):
                curr_choice.append(random.choice(self.list))

        self.last_pick = curr_choice
        return curr_choice

