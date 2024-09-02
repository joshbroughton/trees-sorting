#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    for idx, item in enumerate(items):
        if idx < len(items) - 1 and item > items[idx + 1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Worst case running time is O(n^2), as the inner for loop of n steps would need to run
    n times (in the case the list starts reverse-sorted)
    Best case is O(n), in the case the list starts sorted - no pairs to swap are found on the first pass,
    so only n steps occur

    Memory use is O(1). I was curious if enumarate() and iterating over an iterable causes additional memory use
    compared to the theoretical best case, but in looking into this my understanding is that enumerate yields the
    index, item pairs on the fly and does not store them in static memory anywhere - so the memory use is constant
    and not proportional to the input size """
    # Bubblesort is O(n^2) - the outer loop is in is_sorted in this implementation
    list_is_sorted = False
    while not list_is_sorted:
        list_is_sorted = True
        for idx, item in enumerate(items):
            if idx < len(items) - 1 and item > items[idx + 1]:
                items[idx] = items[idx + 1]
                items[idx + 1] = item
                list_is_sorted = False

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    for i, _ in enumerate(items):
        smallest_index = i
        for j in range(i + 1, len(items)):
            if items[j] < items[smallest_index]:
                smallest_index = j
        smallest_value = items[smallest_index]
        items[smallest_index] = items[i]
        items[i] = smallest_value

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    for i, current in enumerate(items):
        should_shift = False
        for j in range(0, i + 1):
            if should_shift:
                temp = items[j]
                items[j] = last
                last = temp
            elif current < items[j]:
                should_shift = True
                last = items[j]
                items[j] = current
