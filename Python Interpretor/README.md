Fifth is a new stack-based language. A stack is a data structure which can only have elements added to the top. Fifth stores a stack of integers and supports commands to manipulate that stack. Operations always apply to the top of the stack.

Fifth supports the following arithmetic operators:

+ - * /
Each of these applies the operator to the two values on the top of the stack and pushes the result to the top of the stack. If division results in a non-integer, round down.

Fifth also supports the following commands:

PUSH x - push x onto the top of the stack, where x is a valid integer
POP - remove the top element of the stack
SWAP - swap the top two elements of the stack
DUP - duplicate the top element of the stack
Write a python program which works as a fifth interpreter. Each line of input to the program should represent a single fifth command. Output the result of each command to the terminal. Handle errors sensibly.

Example:

stack is []
PUSH 3
stack is [3]
PUSH 11
stack is [3, 11]
+
stack is [14]
DUP
stack is [14, 14]
PUSH 2
stack is [14, 14, 2]
*
stack is [14, 28]
SWAP
stack is [28, 14]
/
stack is [2]
+
ERROR
