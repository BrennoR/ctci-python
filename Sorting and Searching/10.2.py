from collections import Counter
# Group Anagrams


# Time: O(n * |w|log(|w|)), Space: O(n)
def group_anagrams(arr: [str]) -> [str]:
    sorted_arr = []
    counts_dict = {}
    for word in arr:
        cnt = tuple(sorted(Counter(word).items()))
        if cnt in counts_dict:
            counts_dict[cnt].append(word)
        else:
            counts_dict[cnt] = [word]

    for key in counts_dict:
        for word in counts_dict[key]:
            sorted_arr.append(word)

    return sorted_arr


words = ["iceman", "racecar", "manice", "jet", "snake", "koala", "kesna", "carrace", "raccare", "icenam"]
print(group_anagrams(words))
