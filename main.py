from stack import MyStack

if __name__ == '__main__':
    string_bracket = input()
    stack = MyStack()
    is_good = True
    for item in string_bracket:
        if item in '({[':
            stack.push(item)
        elif item in ')}]':
            open_bracket = stack.pop()
            if open_bracket == '(' and item == ')':
                continue
            if open_bracket == '{' and item == '}':
                continue
            if open_bracket == '[' and item == ']':
                continue
            is_good = False
            break

    if is_good and stack.is_empty():
        print('Сбалансированно')
    else:
        print('Несбалансированно')
