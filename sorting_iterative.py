#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time:
        O(n) for all cases as it needs to go through the whole list

    Memory usage:
        O(1), no new list created or other variable creation that is proportional to n
    """
    for idx, item in enumerate(items):
        if idx < len(items) - 1 and item > items[idx + 1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Worst case running time is O(n^2), as the inner for loop of n steps would need to run
    n times (in the case the list starts reverse-sorted). Average case is same.
    Best case is O(n), in the case the list starts sorted - no pairs to swap are found on the first pass,
    so only n steps occur. Real world: Around 2.6s for list of 10000 random ints between 1 andn 1000

    Memory use is O(1). I was curious if enumarate() and iterating over an iterable causes additional memory use
    compared to the theoretical best case, but in looking into this my understanding is that enumerate yields the
    index, item pairs on the fly and does not store them in static memory anywhere - so the memory use is constant
    and not proportional to the input size """
    n = len(items)
    while n > 1:
        new_n = 0
        # reducing the iteration range here instead of using enumerate makes this ~2 times faster in the real world
        for i in range(1, n):
            if items[i - 1] > items[i]:
                temp = items[i - 1]
                items[i - 1] = items[i]
                items[i] = temp
                new_n = i  # Update the position of the last swap
        n = new_n

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Average time complexity is O(n^2) due to the nested loops. Best and worse are also O(n^2) because we always
    fully iterate both loops, even if the list is sorted.
    Real world benchmark with list of 10000 random ints 0 to 1000 is around 1.03 seconds average

    Space complexity is O(1), we modify the list in place and the temp variables are constant space"""
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
    Average time complexity is O(n^2) due to the nested loops. Worst case is same. Best case is O(n),
    for a sorted list the inner loop will execute in constant time
    Real world benchmark with list of 10000 random ints 0 to 1000 is around 0.97 seconds average
    - current real world is 1.03. The improvement to make the best case actually O(n) and match the theoretical
    best case seem to have slightly decreased the average performance.

    Space complexity is O(1), we create some temp variables but they are of constant size"""
    for i, current in enumerate(items):
        j = i - 1

        while j >= 0 and items[j] > current:
            items[j + 1] = items[j]
            j -= 1

        items[j + 1] = current
