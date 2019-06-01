# Sort Stack


# Time - O(N^2), Space - O(N)
def sort_stack(stack: [int]) -> [int]:
    if not stack:
        return stack

    temp_stack = []
    while stack:
        val = stack.pop()

        while temp_stack and temp_stack[-1] > val:
            stack.append(temp_stack.pop())

        temp_stack.append(val)

    while temp_stack:
        stack.append(temp_stack.pop())

    return stack


# reverse_sorted
stack_1 = [1, 2, 3, 4, 5]
print(stack_1)
print(sort_stack(stack_1))

# null and empty stack
print(sort_stack(None))
print(sort_stack([]))

# various inputs
stack_2 = [3, 2, 5, 1, 4]
stack_3 = [8, 9, 6, 7, 3, 8, 0, 10, 24, 46, 7, 8]
print(sort_stack(stack_2))
print(sort_stack(stack_3))

