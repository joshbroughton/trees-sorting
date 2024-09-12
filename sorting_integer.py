#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: Real world: 0.0013s
        Time Complexity: O(n) + O(n) + O(n + m) -> O(n + m), where n is the length of the list and m is the
        size of the range of values
    Memory usage:
        O(m) - we create a list to store the counts (of size m), but copy the output list in place
    """
    max_number = numbers[0]
    min_number = numbers[0]

    # find min_number and max_number, O(n)
    for item in numbers:
        if item < min_number:
            min_number = item
        if item > max_number:
            max_number = item

    # build the count list, O(m) where m is the range between min and max
    counts_list = [0] * (max_number - min_number + 1)

    # determine counts, O(n)
    for item in numbers:
        counts_list[item - min_number] += 1

    i = 0
    j = 0
    # Outer loop is O(m)
    while i < len(counts_list):
        #if the count is > 0, we need to copy another of that value to index j in our output list
        # this loop runs n times total across all iterations - so these nested loops are O(n + m)
        while counts_list[i] != 0:
            numbers[j] = i + min_number
            j += 1
            counts_list[i] -= 1
        i +=1



def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
