from lexer import lexer
from parser import parser

def validate_code(code):
    result = parser.parse(code, lexer=lexer)
    if result is None:
        print("Code has syntax errors.")
    else:
        print("Code is syntactically correct.")
        print("Parsed structure:", result)

def main():
    print("Enter your code below (end input with an empty line):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    code = "\n".join(lines)
    print("\nValidating syntax...\n")
    validate_code(code)

if __name__ == "__main__":
    main()