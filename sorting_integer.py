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
    if len(numbers) == 0:
        return
    min_number, max_number = find_value_range(numbers)

    # build the count list, O(m) where m is the range between min and max
    counts_list = [0] * (max_number - min_number + 1)

    # determine counts, O(n)
    for number in numbers:
        counts_list[number - min_number] += 1

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
    Running time:
        Time complexity is O(n + n + n + n + m) = O(n+m)
        Real world bench is 0.0033 - it was twice as fast to write a new output list
    Memory usage:
        This version mutating the input uses O(n) memory to create the bucket list.
        Writing to a new list is O(n + n), or O(n) as well
    """
    if len(numbers) == 0:
        return
    min_number, max_number = find_value_range(numbers)
    buckets = [[] for _ in range(num_buckets)]
    step = (max_number - min_number + 1) // num_buckets
    if step < 1:
        step = 1

    for number in numbers:
        bucket_index = (number - min_number) // step
        buckets[bucket_index].append(number)

    i = 0
    for bucket in buckets:
        counting_sort(bucket)
        while len(bucket) > 0:
            numbers[i] = bucket.pop(0)
            i += 1


def find_value_range(numbers):
    """
    Helper method to find the range of given numbers
    """
    max_number = min_number = numbers[0]

    # find min_number and max_number, O(n)
    for number in numbers:
        if number < min_number:
            min_number = number
        if number > max_number:
            max_number = number

    return(min_number, max_number)
