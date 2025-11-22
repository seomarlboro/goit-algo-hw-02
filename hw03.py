
def is_symmetric(string):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()

    return len(stack) == 0

def main():
    for string in test_cases:
        result = is_symmetric(string)
        status = '✅ Symmetric\n' if result else '❌ Not symmetric\n'
        print(f'{string}: {status}')


test_cases = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }",
    "((){[]})",
    "((((("
]

if __name__ == '__main__':
    main()