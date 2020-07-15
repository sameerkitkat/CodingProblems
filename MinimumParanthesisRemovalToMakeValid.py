def MinimumParanthesisRemovalToMakeValid(s):
    indexes_to_remove = set()
    stack = []
    for i, c in enumerate(s):
        if c not in "()":
            continue
        if c == "(":
            stack.append(i)
        elif not stack:
            indexes_to_remove.add(i)
        else:
            stack.pop()
    print(indexes_to_remove)
    while stack:
        indexes_to_remove.add(stack.pop())
    print(indexes_to_remove)
    string_builder = ""
    for i, c in enumerate(s):
        if i not in indexes_to_remove:
            string_builder += c
    return string_builder


if __name__ == '__main__':
    s = "lee(t(c)o)d))e)"
    print(MinimumParanthesisRemovalToMakeValid(s))
