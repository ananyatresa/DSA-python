def iterative_subset(nums):
    outer = [[]]

    for num in nums:
        # Iterate through a snapshot of current subsets
        outer_copy = list(outer)
        for subset in outer_copy:
            # Create a new subset by copying the existing one and adding `num`
            new_subset = subset + [num]
            if new_subset not in outer:
                outer.append(new_subset)  # Add the new subset to the list of subsets

    return outer



print(iterative_subset([1,2,2,3, 3]))
