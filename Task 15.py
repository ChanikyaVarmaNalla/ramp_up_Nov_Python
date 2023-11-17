def longest_valid_parentheses(s):
    stack = [-1]
    max_length = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    return max_length

st = ")()(())"
result = longest_valid_parentheses(st)
print("Length of the longest valid parentheses substring:", result)
