# Matlab Syntax Validator

A custom compiler-front-end tool built with Python and PLY (Python Lex-Yacc). This project validates the syntax of core MATLAB-style programming constructs using Lexical Analysis and Parsing.

## Features
This validator checks for correct syntax in the following constructs:

Functions: Formal function declarations with block scoping.

Loops: Supports both for and while loops.

Selection: if and if-else conditional structures.

Statements: Standard print() and return operations.

## Installation
Clone the repository to your local machine.

Install the PLY library:

```Bash
pip install -r requirements.txt
```

## How to Use
Run the main script:

```Bash
python main.py
```

Enter your code in the terminal.

Press Enter on an empty line to trigger the validation.

Sample Input for Testing:
Matlab

```
function myTest() {

    if (x) {
    
        print(x);
        
    } else {
    
        return y;
        
    }
}
```
