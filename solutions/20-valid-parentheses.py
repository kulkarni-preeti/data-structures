def closeParentheses(input):
    # object = "()[]{}"
    stack = []
    obj = { '(' : ')' , '{' : '}', '[' : ']'}

    for s in input:
        if s in obj:
            stack.append(s)
        elif s == obj.get(stack[-1]):
            stack.pop()
        else:
            return False
    
    print(stack)

    return not stack

result = closeParentheses("]")

print(result)
