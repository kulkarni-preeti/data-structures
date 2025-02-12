def closeParentheses(input):
    input = "([]"
    stack = []
    obj = { '(' : ')' , '{' : '}', '[' : ']'}

    for s in input:
        if s in obj:
            stack.append(s)
            print(f"Appended to stack : {stack}")
        elif s == obj.get(stack[-1]):
            print(f"Popped before stack : {stack}")
            stack.pop()
            print(f"Popped from stack : {stack}")
        else:
            return False
    
    print(stack)

    return not stack

result = closeParentheses("]")

print(result)
