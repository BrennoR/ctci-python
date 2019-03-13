# without conversion of string to list
def URLify_1(string):
    count = 0
    for i in range(len(string)):
        j = i + (count * 2)
        if string[j] == " ":
            string = string[:j] + "%20" + string[j + 1:]
            count += 1

    return string


# method from CtCl-6th-Edition-Python repository by careercup
def URLify_2(string, length):
    string = list(string)
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            print(new_index)
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return ''.join(string)


print(URLify_2("He r 33 2rf f        ", 13))
