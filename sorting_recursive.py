#!python

import random
from sorting_iterative import insertion_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time:
        Best Case: O(1), if either list is empty, time is constant independent of the
        size of the remaining list
        Worst/average: O(n), as it will require one pass per item in each list until one is empty
    Memory usage:
        O(n), as we create a new_list of length n
        """
    merged_list = []
    while len(items1) > 0 and len(items2) > 0:
        merged_list.append(items1.pop(0) if items1[0] < items2[0] else items2.pop(0))

    if len(items1) == 0:
        merged_list.extend(items2)
    else:
        merged_list.extend(items1)
    return merged_list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time:
        Same time complexity as underlying sort (O(n^2) / 2 is still O(n^2))
        The O(n) from the merge is ignored as we only use the term with the highest degree
        - Best case O(n) for sorted list
        - Worst and average are O(n^2)
        - Real world benchmark is ~0.5 seconds with 10000 ints 0 to 1000, which is half of
        insertion sort time, which is expected
    Memory use: n/2 + n/2 + n extra lists gives O(n)
    """
    split_index = len(items) // 2
    list1 = items[:split_index]
    list2 = items[split_index:]
    insertion_sort(list1)
    insertion_sort(list2)
    items[:] = merge(list1, list2)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time:
        All cases are O(nlog(n))
        Why? merge is always O(n) (its best case can't happen when we're splitting into equal lists except
        when they are empty, which occurs after n merges)
        and we merge log(n) times - any time we divide that's a log(n) operation. technically its a base 2 log
        but because dividing in 2 is the most common log in time complexity analysis, the base is omitted
        - Real world benchmark 10000 random ints 1-1000 is ~0.02 seconds - blazing fast!
    Memory usage:
        O(n) for the temp split lists created along the way
    """
    if len(items) <= 1:
        return items
    else:
        split_index = len(items) // 2
        list1 = items[:split_index]
        list2 = items[split_index:]
        list1 = merge_sort(list1)
        list2 = merge_sort(list2)
        items[:] = merge(list1, list2)
        return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Pivot method: first item in list
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    pivot = items[low]
    p = None
    while True:
        #look for the first item from the back of the array that is less than the pivot
        while items[high] >= pivot and high > low:
            high = high - 1
        #variations of this conditions mean the paritition is done because the indices have met
        if high <= low:
            items[low] = pivot
            p = low
            break
        #place the item we found into the open space
        items[low] = items[high]
        #same as above but flipped to advance the low index
        while items[low] < pivot and low < high:
            low = low + 1
        if low >= high:
            items[high] = pivot
            p = high
            break

        items[high] = items[low]
    return p

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    if low is None:
        low = 0
    if high is None:
        high = len(items) - 1

    if low >= high:
        return
    else:
        p = partition(items, low, high)
        quick_sort(items, low, p-1)
        quick_sort(items, p+1, high)
