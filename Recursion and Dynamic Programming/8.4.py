# Power Set
# TODO: Implement Combinatorics Solution


# Solution taken from career-cup GitHub repository
def power_set(set, index):
    allSubsets = []
    if len(set) == index:
        if [] not in allSubsets:
            allSubsets.append([])
    else:
        allSubsets = power_set(set, index + 1)
        item = set[index]
        moreSubsets = []
        for subset in allSubsets:
            newSubset = []
            [newSubset.append(value) for value in subset if value not in newSubset]
            newSubset.append(item)
            moreSubsets.append(newSubset)
        [allSubsets.append(value) for value in moreSubsets if value not in newSubset]
    return allSubsets


print(power_set([1, 2, 3, 4, 5], 0))



