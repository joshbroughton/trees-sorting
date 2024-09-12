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
    Running Time:
        O(n) - the while True makes this sort of unintuitive/difficult to reason about. But we can see that the outer loop
        has no fixed dependency on n; the total number depends on the progress of the inner loops. The combined effect
        of these loops is to loop through the whole list once, so the overall time complexity is O(n)
        real world benchmark: 0.008947
    Memory usage:
        O(1), in place partition
    """
    pivot = items[low]
    lo = low + 1
    while True:
        #look for the first item from the back of the array that is less than the pivot
        while lo <= high and items[high] >= pivot:
            high = high - 1
        #look for the first item from the front of the array larger than the pivot
        while lo <= high and items[lo] <= pivot:
            lo = lo + 1
        #if the values cross, break out of the loop
        if high < lo:
            break
        # swap the two out of place items
        items[lo], items[high] = items[high], items[lo]

    #swap the pivot into its place
    items[low], items[high] = items[high], items[low]
    return high

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time:
        O(nlog(n)) - when the pivot splits the list neatly down the middle we get the best case time. If we visualize
        each recursive partition as a branch in a tree, we get the shortest tree (of height logn) when we get even
        partitions at each branch.
    Worst case running time:
        O(n^2) - This occurs when the partition at each step is at one extreme of the list, as would happen
        in this implementation when the list is already sorted or reverse sorted. Imagining a tree again, the partitions
        in this case would create a completely unbalanced tree, whose height would be (O(n)) - * O(n) for partition call
        gives O(n^2)
    Memory usage:
        O(logn) - Recursive methods have a space complexity caused by the recursion stack and equal to the recursion
        depth.
    """
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
